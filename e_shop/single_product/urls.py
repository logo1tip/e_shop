from django.urls import path
from single_product.views import single_product


urlpatterns = [
    path("", single_product, name="products_page"),
]
