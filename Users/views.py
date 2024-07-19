from rest_framework import viewsets
from .models import Shop
from market.serializers import ProductsListSerializer
from .serializer import UserShopSerializer
from Base.permissions import IsShopOwnerOrNewShop

class UserShopViewSet(viewsets.ModelViewSet):
    serializer_class = UserShopSerializer
    permission_classes = [IsShopOwnerOrNewShop]
    def get_queryset(self):
        return Shop.objects.filter(owner=self.request.user)
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
class UserProductViewSet(viewsets.ModelViewSet):
    pass