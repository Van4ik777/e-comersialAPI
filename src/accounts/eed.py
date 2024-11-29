from products.models import Category, Product, ProductDetail
from django.contrib.auth import get_user_model
from products.models import Review

User = get_user_model()

def run():
    # Создаем категории
    electronics = Category.objects.create(name="Electronics")
    furniture = Category.objects.create(name="Furniture")

    # Создаем продукты
    laptop = Product.objects.create(
        name="Laptop",
        category=electronics,
        price=1200.00,
        discount=100.00,
        description="High-performance laptop"
    )
    sofa = Product.objects.create(
        name="Sofa",
        category=furniture,
        price=800.00,
        discount=50.00,
        description="Comfortable sofa"
    )

    # Добавляем детали к продуктам
    ProductDetail.objects.create(
        product=laptop,
        colors=["black", "gray"],
        materials=["aluminum", "plastic"],
        height=2.5,
        width=15.0,
        depth=10.0,
        swivel_mechanism=False
    )
    ProductDetail.objects.create(
        product=sofa,
        colors=["blue"],
        materials=["fabric", "wood"],
        height=35.0,
        width=80.0,
        depth=35.0,
        swivel_mechanism=False
    )

    # Создаем пользователей
    user1 = User.objects.create_user(username="john_doe", password="password123", city="New York")
    user2 = User.objects.create_user(username="jane_doe", password="password456", city="Los Angeles")

    # Добавляем отзывы
    Review.objects.create(user=user1, text="Amazing laptop!", product_id=laptop.id)
    Review.objects.create(user=user2, text="Very comfortable sofa!", product_id=sofa.id)
