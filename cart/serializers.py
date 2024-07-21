from rest_framework import serializers
from .models import *

class CartItemsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="product.name", read_only=True)
    price = serializers.CharField(source="product.price", read_only=True)
    shop = serializers.CharField(source="product.shop.name", read_only=True)
    class Meta:
        model = CartItem
        fields = ["name", "price", "shop", "product"]