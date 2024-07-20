from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    re_path(r'^auth/', include('djoser.urls')),
    path('own-shop/', UserShopViewSet.as_view({"get": "retrieve", "post": "create", "put": "update"})),
]