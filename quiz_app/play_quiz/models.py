from django.db import models
from django.utils.translation import gettext as _


class Quiz(models.Model):
    """Object to hold a quiz, consisting of multiple questions"""
    name = models.TextField(_("Name of the quiz"), max_length=100)

    def __str__(self):
        return f"{self.name}"


class Question(models.Model):
    """Object to hold a question, consisting of multiple choices"""
    MIN_NUMBER_OF_QUESTION_PER_QUIZ = 3
    MAX_NUMBER_OF_QUESTION_PER_QUIZ = 15
    ALLOWED_NUMBER_OF_CORRECT_CHOICES = 1

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField(_("Question text"), max_length=100)

    def __str__(self):
        return f"{self.quiz}: {self.text}"


class Choice(models.Model):
    """Object to hold a choice related to a question"""
    MAX_CHOICES_COUNT = 4

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(_("Choice text"), max_length=100)
    is_correct = models.BooleanField(_("Is the choice correct"), default=False, null=False)

    def __str__(self):
        return f"{self.question}: {self.text}"
