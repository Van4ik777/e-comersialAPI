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

        params = self.request.query_params
        for key, value in params.items():
            if key == "category_id":
                queryset = queryset.filter(category_id=value)
            elif key == "name":
                queryset = queryset.filter(name__icontains=value)
            elif key == "min_price":
                queryset = queryset.filter(price__gte=value)
            elif key == "max_price":
                queryset = queryset.filter(price__lte=value)

        return queryset

    @action(detail=False, methods=["get"], url_path="filter")
    def filter_products(self, request):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response(
                {"message": "No products found matching your criteria."},
                status=404
            )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
