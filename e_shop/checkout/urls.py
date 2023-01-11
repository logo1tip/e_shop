from django.urls import path
from checkout.views import checkout_page


urlpatterns = [
    path("", checkout_page, name="checkouts_page"),
]
