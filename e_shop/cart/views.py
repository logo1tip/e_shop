from django.shortcuts import render


def cart_page(request):
    return render(request, "carts.html", {})