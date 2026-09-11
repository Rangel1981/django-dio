from django.contrib import admin
from .models import Question, Choice


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass