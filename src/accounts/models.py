from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from products.models import Product


class User(AbstractUser):
    city = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name="custom_user_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="custom_user_permissions_set",
        blank=True
    )

    def __str__(self):
        return self.username

    def get_favorite_products(self):
        from ..products.models import Product

        return Product.objects.filter(user=self)


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField()

    def __str__(self):
        return f"Review by {self.user} on {self.product}"

    @property
    def product(self):
        from ..products.models import Product  # Lazy import
        return Product.objects.get(id=self.product_id)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    products = models.ManyToManyField(Product, blank=True)


class Favourite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="favourite")
    products = models.ManyToManyField(Product, blank=True)