from django.db import models



class Product(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name="Name",   
    )
    slug = models.SlugField(
        unique=True,
    )
    image = models.ImageField(
        verbose_name="Image",
    )
    description = models.TextField(
        verbose_name="Description",
        null=True,
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name="Price",
    )

    def __str__(self):
        return self.title
