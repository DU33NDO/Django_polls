from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "kaspi"
router = DefaultRouter()
router.register("good", views.APIGoodViewSet)
router.register("magazin", views.APIMagazinViewSet)

urlpatterns = [
    path("home/", views.CacheTry, name="ex_cache"),
    # path("api/get_goods/", views.api_goods_2, name="for_api"),
    # path("api/good_detail/<int:pk>/", views.api_good_detail, name="detail_good"),
    # path("api/get_goods/", views.APIGoods_new.as_view(), name="for_api"),
    # path(
    #     "api/good_detail/<int:pk>/",
    #     views.APIGoodDetail_new.as_view(),
    #     name="detail_good",
    # ),
    path("api/", include(router.urls)),
    # path("read/", views.APIMagazinViewSet.as_view(), name="store_api"),
]
