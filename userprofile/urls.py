from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path

from . import views

app_name = "lol"

urlpatterns = [
    path("cv_upload/", views.UploadCV.as_view(), name="cv_upload"),
    path("success", views.success, name="success"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
