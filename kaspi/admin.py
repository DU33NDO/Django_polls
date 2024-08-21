from django.contrib import admin
from .models import Magazin, Good, MagazinGoods, Review, For_Good

admin.site.register(Good)
# admin.site.register(kaspiObject)
admin.site.register(Magazin)
admin.site.register(MagazinGoods)
admin.site.register(For_Good)
admin.site.register(Review)