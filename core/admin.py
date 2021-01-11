from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Questions, Answers, QuestionGroups

admin.site.register(User, UserAdmin)

class AnswerInline(admin.TabularInline):
    model = Answers


class QuestionsAdmin(admin.ModelAdmin):

    inlines = [AnswerInline]
    class Meta:
        model = Questions


class QuestionGroupsAdmin(admin.ModelAdmin):

    class Meta:
        QuestionGroups

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(QuestionGroups, QuestionGroupsAdmin)
