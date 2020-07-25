from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Test(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField(max_length=120)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:30]


class Answer(models.Model):
    text = models.CharField(max_length=120)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:30]


class Result(models.Model):
    result = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)