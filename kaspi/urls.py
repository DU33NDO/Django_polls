from django.urls import path, re_path
from . import views

app_name = "kaspi"

urlpatterns = [
    path("home/", views.CacheTry, name="ex_cache"),
    path("api/get_goods/", views.api_goods_2, name="for_api"),
    path("api/good_detail/<int:pk>/", views.api_good_detail, name="detail_good"),
]
