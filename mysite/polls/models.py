import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=100, verbose_name="Имя", blank=True)
    surname = models.CharField(max_length=100, verbose_name="Фамилия", blank=True)
    username = models.CharField(max_length=100, verbose_name="Логин", unique=True)
    mail = models.EmailField(verbose_name="Ваша почта", unique=True)
    password = models.CharField(max_length=100, verbose_name="Пароль")
    password2 = models.CharField(max_length=100, verbose_name="Повторите пароль")
    avatar = models.ImageField(verbose_name="Загрузите аватарку", upload_to='avatars')


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
