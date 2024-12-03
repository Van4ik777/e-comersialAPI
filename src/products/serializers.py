from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product, Category, ProductDetail

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'discount', 'description', 'images', 'category']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ['colors', 'materials', 'height', 'width', 'depth', 'swivel_mechanism']


