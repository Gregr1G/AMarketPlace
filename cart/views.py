from rest_framework import viewsets, permissions
from .serializers import *

class UserCartViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(buyer=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(buyer=self.request.user)

    def get_object(self):
        return CartItem.objects.get(product=self.kwargs["pk"])

