from django.urls import path
from .views import *

urlpatterns = [
    path('product/<slug:slug>/', PublicProductsApiView.as_view()),
    path('shop/<name>/', PublicProductsListByShopApiView.as_view()),
    path('category/', PublicCategoryListApiView.as_view()),
    path('category/<slug:slug>/', PublicProductsByCategoryViewSet.as_view({"get": "retrieve"}))
]