from django.urls import path
from .views import *

urlpatterns = [
    path('product/<int:pk>/', PublicProductsApiView.as_view()),
    path('category-list/', PublicCategoryListApiView.as_view()),
    path('category/<int:pk>/', PublicProductsByCategoryViewSet.as_view({"get": "retrieve"}))
]