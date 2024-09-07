from django.contrib import admin

from .models import Question, Choice


class PersonAdmin(admin.ModelAdmin):
    list_display = ("name",)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "question_text", "pub_date", "comment")
    actions = ("add_comment",)

    def add_comment(self, request, queryset):
        for rec in queryset:
            rec.question_text += ", bro"
            rec.save()
        self.message_user(request, "готово")


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
