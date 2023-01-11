from django.db import models
from user.models import User
from single_product.models import Product


class Cart(models.Model):

    owner = models.ForeignKey(
        User,
        null=True, 
        verbose_name="Customer",
        on_delete=models.CASCADE,
    )
    products = models.ManyToManyField(
        Product,
        blank=True,
    )
    total_products = models.PositiveBigIntegerField(
        default=0,
    )
    final_price = models.DecimalField(
        max_digits=9,
        default=0,
        decimal_places=2,
        verbose_name="Total price",
    )
    in_order = models.BooleanField(
        default=False,
    )
    for_anonymous_user = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return str(self.id)


