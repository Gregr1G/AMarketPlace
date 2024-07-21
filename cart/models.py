from django.db import models
from django.contrib.auth.models import User
from market.models import Product


class CartItem(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
