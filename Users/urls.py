from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    # re_path(r'^auth/', include('djoser.urls')),
    # path('own-shop/<int:pk>/', UserShopViewSet.as_view({"put": "update"})),
    path('own-shop/', UserShopViewSet.as_view({"get": "list", "post": "create"})),
]