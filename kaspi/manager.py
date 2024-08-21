from django.db import models
from django.utils.timezone import now

class CustomQuerySet(models.QuerySet):
    def order_by_name(self):
        return self.order_by(name)

class CustomMagazinManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(created_date__gte=now)

class CustomGoodManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(price__gte=1200)