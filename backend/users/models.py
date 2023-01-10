from django.db import models
from django.contrib.auth.models import AbstractUser as DjangoUser
from django.core.validators import RegexValidator


class User(DjangoUser):
    avatar = models.ImageField(upload_to="media/", blank=True, null=True)
    discord = models.CharField(max_length=20, blank=True, null=True)
    telegram = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=20, validators=[RegexValidator(',.*', inverse_match=True)], unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return '{}+{}'.format(self.username, self.discord)
