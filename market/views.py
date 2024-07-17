from rest_framework import generics, viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class PublicProductsApiView(generics.RetrieveAPIView):
    serializer_class = ProductsListSerializer
    lookup_field = "slug"
    queryset = Product.objects.all()

class PublicCategoryListApiView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

class PublicProductsByCategoryViewSet(viewsets.ViewSet):
    serializer_class = ProductsListSerializer
    def retrieve(self, request, slug=None):
        product_list = Product.objects.all()
        queryset = set()
        pk = get_object_or_404(Category, slug=slug)
        for i in product_list:
            if pk.id in [cat.id for cat in list(i.category.get_ancestors(ascending=False, include_self=True))]:
                queryset.add(i)

        serializer = ProductsListSerializer(queryset, many=True)
        return Response(serializer.data)

class PublicProductsListByShopApiView(generics.ListAPIView):
    serializer_class = ProductsListSerializer
    queryset = Product.objects.all()
    def get_queryset(self):
        return Product.objects.filter(shop=get_object_or_404(Shop, name=self.kwargs["name"]))


