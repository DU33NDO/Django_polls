from django.db import models


class commonInfoText(models.Model):
    pages = models.PositiveIntegerField(blank=False)
    author = models.CharField(max_length=200)
    number_of_purchases = models.PositiveIntegerField(blank=False)

    class Meta:
        abstract = True


class Book(commonInfoText):
    rate = models.FloatField()

    def __str__(self) -> str:
        return self.author


class NewsPapper(commonInfoText):

    def __str__(self) -> str:
        return self.author


# class Magazine(commonInfoText):
#     QTYPE = {
#         "F": "Fashion",
#         "B": "Business",
#         "S": "Scinetific",
#     }
#     type = models.CharField(max_length=100, choices=QTYPE)

#     def __str__(self) -> str:
#         return self.author


class commonInfoPerson(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    salary = models.PositiveIntegerField()
    address = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Journalist(commonInfoPerson):
    newspappers = models.ManyToManyField(NewsPapper)

    def __str__(self) -> str:
        return self.name


class Redactor(commonInfoPerson):
    books = models.ManyToManyField(Book)

    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    newsPappers = models.ForeignKey(NewsPapper, on_delete=models.CASCADE)
