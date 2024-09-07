from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("social_django.urls", namespace="social")),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("polls/", include("polls.urls", namespace="plsNamespace")),
    path("kaspi/", include("kaspi.urls", namespace="pooik")),
    # path("userprof/", include("userprofile.urls")),
]
