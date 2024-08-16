from django.contrib import admin

from .models import (
    commonInfoPerson,
    commonInfoText,
    Book,
    NewsPapper,
    # Magazine,
    Journalist,
    Redactor,
    Article,
)

admin.site.register(Book)
admin.site.register(NewsPapper)
# admin.site.register(Magazine)
admin.site.register(Journalist)
admin.site.register(Redactor)
admin.site.register(Article)
