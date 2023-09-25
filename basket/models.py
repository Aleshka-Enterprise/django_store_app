from django.db import models
from user.models import User
from products.models import Product


class BasketQuerySet(models.QuerySet):

    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Продукт')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    objects = BasketQuerySet.as_manager()

    def sum(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'Корзина пользователя {self.user.username}'
