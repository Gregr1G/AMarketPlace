from rest_framework import viewsets
from .models import Shop
from django.shortcuts import get_object_or_404
from .serializer import UserShopSerializer
from Base.permissions import IsShopOwnerOrNewShop

class UserShopViewSet(viewsets.ModelViewSet):
    serializer_class = UserShopSerializer
    permission_classes = [IsShopOwnerOrNewShop]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return get_object_or_404(Shop, owner=self.request.user)

    def get_object(self):
        return self.get_queryset()
