from django.urls import path, include
from .views import *

urlpatterns = [
    path("cart/", UserCartViewSet.as_view({"get": "list", "post": "create"})),
    path("cart/<int:pk>/", UserCartViewSet.as_view({"delete": "destroy"}))
]