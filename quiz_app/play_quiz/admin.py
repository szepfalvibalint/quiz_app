from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Quiz, Question, Choice
from nested_admin import NestedModelAdmin, NestedTabularInline


class ChoiceInline(NestedTabularInline):
    model = Choice
    extra = 0
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1})},
    }


class QuestionInline(NestedTabularInline):
    model = Question
    inlines = [ChoiceInline]
    extra = 0
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1})},
    }


class QuizAdmin(NestedModelAdmin):
    model = Quiz
    inlines = [QuestionInline]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1})},
    }


admin.site.register(Quiz, QuizAdmin)
