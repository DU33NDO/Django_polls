from xml.etree.ElementInclude import include
from django.urls import path, re_path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page

from . import views

app_name = "polls"
urlpatterns = [
    re_path(r"^index/$", views.index, name="index"),
    path("<int:question_id>/", views.QuestionRedirectView.as_view(), name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("all", views.all, name="all"),
    path("first/<int:question_number>/", views.number, name="firsr-N"),
    path("create/", views.create, name="create"),
    path("delete/", views.delete, name="delete"),
    path("change/", views.change, name="change"),
    path("choice-question/", views.choice_to_question, name="choice-to-question"),
    path("question-choice/", views.question_to_choice, name="question-to-choice"),
    path("latest/", views.latest, name="latest"),
    path("count/", views.count, name="count"),
    path("agregate/", views.agregate, name="agregate"),
    path("annotate/", views.annotate, name="anotate"),
    path("avg/", views.avg, name="avg"),
    path("concat/", views.concat, name="concat"),
    path("all_questions", views.all_questions, name="all_questions"),
    path("delete_id/<int:question_number>", views.delete_id, name="delete-by-id"),
    path("find/<str:question_str>/", views.get_question, name="find-question"),
    path("get_id/<int:question_id>", views.get_id, name="get_by_id"),
    path("hello", views.HelloWorld.as_view(), name="hello-world"),
    path("detail-first", views.QuestionDetailView.as_view(), name="detail-first"),
    path("detail/<int:pk>", views.QuestionDetail.as_view(), name="question-detail"),
    path("list", views.QuestionList.as_view(), name="list-question"),
    path("choice-list/<int:vote>", views.ChoiceListView.as_view(), name="choice-list"),
    path("q_formview", views.QuestionFormView.as_view(), name="q-formV"),
    path("q_createview", views.QuestionCreateView.as_view(), name="q-createV"),
    path(
        "q_updateview/<int:pk>/", views.QuestionUpdateView.as_view(), name="q-updateV"
    ),
    path("q_deletev/<int:pk>/", views.QuestionDeleteView.as_view(), name="q-deleteV"),
    path("q_paginator", views.paginator, name="q-paginator"),
    path(
        "login",
        LoginView.as_view(template_name="polls/login.html", next_page="polls:index"),
        name="polls/login",
    ),
    path("logout", LogoutView.as_view(next_page="polls:index"), name="logout"),
    path(
        "password_change",
        PasswordChangeView.as_view(
            template_name="polls/change_password.html",
            success_url=reverse_lazy("polls:polls/password_change_done"),
        ),
        name="password_change",
    ),
    path(
        "password_change_done",
        PasswordChangeDoneView.as_view(template_name="polls/password_changed.html"),
        name="password_changed",
    ),
    path(
        "password_reset",
        PasswordResetView.as_view(
            template_name="polls/reset_password.html",
            subject_template_name="polls/reset_subjet.txt",
            email_template_name="polls/reset_email.txt",
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done",
        PasswordResetDoneView.as_view(template_name="polls/password_reset_done.html"),
        name="password_reset_done",
    ),
    path("check_middleware", views.check_custom_middleware, name="check_middleware"),
    path("class_middle", views.chect_class_middleware, name="class_middleware"),
    path("email_send", views.send_email, name="send_email"),
    path("contact/thanks/", views.thanks, name="thanks"),
]
