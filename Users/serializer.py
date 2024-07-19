from rest_framework import serializers
from .models import *

class UserShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ["name", "description", "logo"]

