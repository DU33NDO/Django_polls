from django.contrib import admin
from .models import Magazin, Good, MagazinGoods

admin.site.register(Good)
admin.site.register(Magazin)
admin.site.register(MagazinGoods)