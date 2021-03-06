from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=225)
    question_description = models.CharField(max_length=225, default="Basic migrations")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_answer = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question} --->  {self.choice_answer}"
