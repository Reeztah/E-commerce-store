from django.db import models
from profiles.models import User
from products.models import Product


class ShopCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class ShopCartItem(models.Model):
    shopcart = models.ForeignKey(ShopCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_add = models.DateTimeField(auto_now_add=True)
