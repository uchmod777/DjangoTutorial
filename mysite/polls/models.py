"""
Models for the database objects being used by the polls app.
"""

import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    """Question model for poll app."""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    objects = models.Manager() #pylint for django was not detecting the objects field
    # (each class inheriting from models.Model should have an objects field defined)

    def __str__(self):
        return str(self.question_text)

    def was_published_recently(self):
        """Checks if the question was recently published."""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    """Choice model for poll app."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)
