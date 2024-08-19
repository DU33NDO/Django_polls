from django.db import models
from django.contrib.auth.models import User

class Good(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Magazin(models.Model):
    name = models.CharField(max_length=256)
    created_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=256)
    goods = models.ManyToManyField(to=Good, through='MagazinGoods', through_fields=('magazin', 'good'))
    staff = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class MagazinGoods(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    magazin = models.ForeignKey(Magazin, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.good} in {self.magazin}"
