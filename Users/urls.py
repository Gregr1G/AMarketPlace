from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    path('own-shop/', UserShopViewSet.as_view({"get": "retrieve", "post": "create", "put": "update"})),
]