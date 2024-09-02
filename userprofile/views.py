from .forms import CvForm
from .models import UserProf
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse
from django.http import HttpResponse


def success(request, pk):
    user_prof = get_object_or_404(UserProf)
    return render(request, "success.html", {"user_prof": user_prof})


class UploadCV(CreateView):
    model = UserProf
    template_name = "userprofile/add.html"
    form_class = CvForm

    def get_success_url(self) -> str:
        return reverse("lol:success")
