from itertools import chain
from django.shortcuts import render
from .models import Wine, Food


def view_products(request):
    """
    A view to display the shop's products and to handle
    sorting and search queries
    """

    wines = Wine.objects.all()
    foods = Food.objects.all()
    all_products = list(chain(wines, foods))
    print(all_products)

    context = {
        'products': all_products
    }

    return render(request, 'products/products.html', context)
