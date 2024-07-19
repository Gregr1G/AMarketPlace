from django.db import models
from django.contrib.auth.models import User
from Base.servises import get_upload_logo_path

class Shop(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название магазина', unique=True)
    logo = models.ImageField(upload_to=get_upload_logo_path, blank=True, verbose_name='Logo')
    description = models.TextField(blank=True, verbose_name='Описание магазина')
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    pass


