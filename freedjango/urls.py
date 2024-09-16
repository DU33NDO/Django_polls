from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", include("social_django.urls", namespace="social")),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("polls/", include("polls.urls", namespace="plsNamespace")),
    path("kaspi/", include("kaspi.urls", namespace="pooik")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("userprof/", include("userprofile.urls")),
]
