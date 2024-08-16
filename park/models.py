from django.db import models
import datetime


class PersonExample(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(default=datetime.date.today)

    class Meta:
        abstract = True


class Parent(PersonExample):
    post = models.TextField()

    def __str__(self) -> str:
        return self.name


class Child(PersonExample):
    is_under_18 = models.BooleanField(default=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


# class IceCream(models.Model):
#     # qtype = {"C": "Chocolate", "V": "Vanilla", "M": "Mint"}
#     # flavor = models.CharField(choices=qtype, max_length=200)
#     price = models.IntegerField()

#     def __str__(self) -> str:
#         return self.flavor


# class IceCreamKiosk(models.Model):
#     address = models.CharField(max_length=200)
#     IceCream = models.ManyToManyField(IceCream, related_name="iceCreams")

#     def __str__(self) -> str:
#         return self.address
