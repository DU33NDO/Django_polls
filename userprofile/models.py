from django.db import models
from django.contrib.auth.models import User


# def user_directory_path(instance, filename):
#     return "user_{0}/{1}".format(instance.user.id, filename)


class UserProf(models.Model):
    cv = models.FileField(upload_to="djangoEx")
    photo = models.ImageField()
    id_photo = models.ImageField()
