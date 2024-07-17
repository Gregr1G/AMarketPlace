from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название магазина', unique=True)
    description = models.TextField(blank=True, verbose_name='Описание магазина')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
