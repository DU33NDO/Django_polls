from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .manager import CustomGoodManager, CustomMagazinManager, CustomQuerySet


class Good(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    price = models.IntegerField()
    reviews = GenericRelation('Review', default='234')
    objects = CustomGoodManager()

    def __str__(self):
        return self.name

@receiver(post_save, sender=Good)
def post_save_dispatcher(sender, **kwargs):
    if kwargs['created']:
        print(f'Товар был успешно добавлен!!')
    
@receiver(post_delete, sender=Good)
def post_delete_dispatcher(sender, **kwargs):
    print(f'Товар был успешно удален(((((')

class Magazin(models.Model):
    name = models.CharField(max_length=256)
    created_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=256)
    goods = models.ManyToManyField(to=Good, through='MagazinGoods', through_fields=('magazin', 'good'))
    staff = models.ManyToManyField(User)
    reviews = GenericRelation('Review', default='234')
    objects = CustomMagazinManager()
    
    # class Meta: 
    #     abstract = True

    def __str__(self):
        return self.name


# class kaspiObject(Magazin):
#     description = models.CharField(max_length=256)

class MagazinGoods(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    magazin = models.ForeignKey(Magazin, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.good} in {self.magazin}"

class Review(models.Model):
    content = models.TextField(max_length=256)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field='content_type', fk_field='object_id')

class For_Good(Good):
    class Meta:
        proxy = True
        ordering = ['name']
