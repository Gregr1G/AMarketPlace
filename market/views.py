from rest_framework import generics, viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
class PublicProductsApiView(generics.RetrieveAPIView):
    serializer_class = ProductsListSerializer
    queryset = Product.objects.all()

class PublicCategoryListApiView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

class PublicProductsByCategoryViewSet(viewsets.ViewSet):
    serializer_class = ProductsListSerializer
    def retrieve(self, request, pk=None):
        product_list = Product.objects.all()
        queryset = set()
        for i in product_list:
            if pk in [cat.id for cat in list(i.category.get_ancestors(ascending=False, include_self=True))]:
                queryset.add(i)

        serializer = ProductsListSerializer(queryset, many=True)
        return Response(serializer.data)

