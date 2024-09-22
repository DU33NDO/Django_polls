# from curses.ascii import HT
from errno import ESTALE
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from pyexpat import model
from random import choices
from re import template
import re
from statistics import mode
from unittest import loader
from django.forms.forms import BaseForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse, reverse_lazy
from django.db.models import Max, Min, Avg, F, Value
from django.db.models.functions import Concat
from .models import Question, Choice
from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from django.core.mail import BadHeaderError, send_mail


from .forms import QuestionForm


def index(request):
    custom = request.my_custom_attr_2
    return render(request, "polls/base.html", {"middleware": custom})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    return HttpResponse("You re looking at the results of question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("You re voting on question %s." % question_id)


def all(requets):
    return HttpResponse(Question.objects.all())


def number(request, question_number):
    questions = Question.objects.all()[:question_number]
    return render(request, "polls/firstToN.html", {"questions": questions})


def create(request):
    q = Question()
    q.question_text = "Today?"
    q.save()
    return HttpResponse("Question created")


def delete(request):
    q = Question.objects.last()
    q.delete()
    return HttpResponse("Question deleted")


def change(requuest):
    q = Question.objects.last()
    q.question_text = "Not today?"
    q.save()
    return HttpResponse("Question changed")


def choice_to_question(request):
    q = Question.objects.last()
    c = Choice()
    c.question = q
    c.choice_text = "not today"
    c.save()
    return HttpResponse("Question был привязан к Choice")


def get_id(request, question_id):
    if question_id < 100:
        q = Question.objects.get(pk=question_id)
        return HttpResponse(q.question_text)
    else:
        # return HttpResponseRedirect(reverse("polls:latest"))
        return redirect("polls:latest")


def question_to_choice(request):
    q = Question.objects.last()
    c = Choice.objects.last()
    q.choice_set.add(c)
    q.save()
    return HttpResponse("Choice был привязан к Question")


def latest(request):
    return HttpResponse(Question.objects.latest("question_text"))


def count(request):
    return HttpResponse(Question.objects.count())


def agregate(request):
    result = Choice.objects.aggregate(votes_min=Min("votes"), votes_max=Max("votes"))
    return HttpResponse(f"MAX:{result['votes_max']}. MIN:{result['votes_min']}")


def annotate(request):
    annotated_choices = Choice.objects.annotate(min_votes=Min("votes"))
    return HttpResponse(annotated_choices.values("id", "choice_text", "min_votes"))


def avg(request):
    avg_choices = Choice.objects.annotate(avg_votes=Avg("votes"))
    return HttpResponse(avg_choices.values("avg_votes"))


def concat(request):
    concat_questions = Question.objects.annotate(
        concat_question=Concat(
            F("question_text"), Value(","), Value(" понятен ли вам вопрос?")
        )
    )
    return HttpResponse(concat_questions.values_list("concat_question"))


def all_questions(request):
    return HttpResponse(Question.objects.values_list("question_text"))


def delete_id(request, question_number):
    try:
        q = Question.objects.get(pk=question_number)
        q.delete()
        return HttpResponse("Succes")
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Такого обьекта не существует")


def get_question(request, question_str):
    q = Question.objects.filter(question_text__icontains=question_str)
    return HttpResponse(q if len(q) > 0 else "Does not exist")


class HelloWorld(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("hello world!")


class QuestionDetailView(TemplateView):
    template_name = "polls/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["question"] = Question.objects.all().first()
        return context


class QuestionRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = "polls:detail-first"

    def get_redirect_url(self, *args, **kwargs):
        try:
            question = Question.objects.get(pk=kwargs["question_id"])
            return reverse("polls:vote", kwargs=kwargs)
        except ObjectDoesNotExist:
            kwargs.pop("question_id")
            return super().get_redirect_url(*args, **kwargs)


class QuestionDetail(DetailView):
    template_name = "polls/detail.html"
    model = Question


class QuestionList(LoginRequiredMixin, ListView):
    template_name = "polls/list.html"
    paginate_by = 2
    model = Question
    login_url = reverse_lazy("polls:polls/login")


class ChoiceListView(ListView):
    model = Choice
    template_name = "polls/choice.html"

    def get_queryset(self, **kwargs):
        q = Choice.objects.filter(votes__gt=self.kwargs["vote"])
        return q


class QuestionFormView(FormView):
    form_class = QuestionForm
    template_name = "polls/questionform.html"
    success_url = "polls:detail"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self) -> str:
        return self.object.instance.get_absolute_url()


class QuestionCreateView(CreateView):
    model = Question
    fields = "__all__"
    template_name = "polls/questionform.html"


class QuestionUpdateView(UpdateView):
    model = Question
    template_name = "polls/update.html"
    fields = "__all__"


class QuestionDeleteView(DeleteView):
    model = Question
    success_url = "polls:list"


def paginator(request):
    q = Question.objects.all()
    paginator = Paginator(q, 2)
    if "page" in request.GET:
        page_num = request.GET.get("page")
    else:
        page_num = 1
    page_obj = paginator.get_page(page_num)
    return render(request, "polls/paginator.html", {"page_obj": page_obj})


def check_custom_middleware(request):
    custom_atr = request.my_custom_attr
    if "counter" in request.COOKIES:
        cnt = int(request.COOKIES["counter"]) + 1
    else:
        cnt = 1
    response = HttpResponse("Here the total views: ")
    response.set_cookie("counter", cnt)
    return response
    # return HttpResponse(f"Here: {custom_atr}")


def chect_class_middleware(request):
    custom_atr = request.my_custom_attr_2
    return HttpResponse(f"Here_2: {custom_atr}")


def send_email(request):
    subject = request.POST.get("subject", "ayo salam")
    message = request.POST.get("message", "меняй пароль")
    from_email = request.POST.get("from_email", "123@example.ru")
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ["admin@example.com"])
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        return HttpResponseRedirect("contact/thanks/")
    else:
        return HttpResponse("Make sure all fields are entered and valid.")


def thanks(request):
    return HttpResponse("Thank u")

class UserListView(ListView):
    model = User
    template_name = "polls/user_list.html"
    context_object_name = "users"
    paginate_by = 10

    def get_queryset(self):
        username = self.request.GET.get('username')
        if username:
            return User.objects.filter(username=username)
        return super().get_queryset()


class UserDetailView(DetailView):
    model = User
    template_name = "polls/user_detail.html"
    context_object_name = "user"
