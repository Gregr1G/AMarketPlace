from rest_framework import permissions
from Users.models import Shop

class IsShopOwnerOrNewShop(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner

class UserShopExist(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return Shop.objects.filter(owner=request.user).exists()
