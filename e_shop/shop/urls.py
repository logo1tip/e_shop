from django.urls import path
from shop.views import shop_page


urlpatterns = [
    path("", shop_page, name="shops_page"),
]
