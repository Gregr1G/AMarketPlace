from rest_framework import serializers
from .models import *
class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "image", "price", "shop", "category", "slug"]

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]