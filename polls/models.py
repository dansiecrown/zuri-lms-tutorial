from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=225)
    pub_date = models.DateTimeField(auto_now_add=True)

class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_answer = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)