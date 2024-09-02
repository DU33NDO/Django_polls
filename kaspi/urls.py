from django.urls import path, re_path
from . import views

app_name = "kaspi"

urlpatterns = [
    path("home/", views.CacheTry, name="ex_cache" )
]