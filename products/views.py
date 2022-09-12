from django.shortcuts import render, get_object_or_404
from .models import Wine, Food


def view_products(request):
    """
    A view to display the shop's products and to handle
    sorting and search queries.
    """

    wines = Wine.objects.all()
    foods = Food.objects.all()

    context = {
        'wines': wines,
        'foods': foods
    }

    return render(request, 'products/products.html', context)


def view_wine_details(request, wine_id):
    """
    A view to display full details for each wine.
    """

    wine = get_object_or_404(Wine, pk=wine_id)

    context = {
        'wine': wine
    }

    return render(request, 'products/wine_details.html', context)



