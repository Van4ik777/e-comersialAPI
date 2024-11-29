from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product, Category, ProductDetail
from .serializers import (
    ProductSerializer, CategorySerializer, ProductDetailSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get("category_id")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    #@action(detail=False, methods=["get"], url_path="by-category")
    #def list_by_category(self, request):
    #    category_id = request.query_params.get("category_id")
    #    if not category_id:
    #        return Response(
    #            {"error": "category_id parameter is required"},
    #            status=400
    #        )
    #    products = Product.objects.filter(category_id=category_id)
    #    serializer = self.get_serializer(products, many=True)
    #    return Response(serializer.data)


class ProductDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
