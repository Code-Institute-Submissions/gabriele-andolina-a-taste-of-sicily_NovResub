from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Wine, Food


def view_products(request):
    """
    A view to display the shop's products and to handle
    sorting and search queries.
    """

    wines = Wine.objects.all()
    foods = Food.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Don't forget to tell us what you're looking for!")
                return redirect(reverse('all_products'))

            queries = Q(product_type__icontains=query) | Q(description__icontains=query)
            wines = wines.filter(queries)
            foods = foods.filter(queries)

    context = {
        'wines': wines,
        'foods': foods,
        'search_term': query,
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


def view_food_details(request, food_id):
    """
    A view to display full details for each food product.
    """

    food = get_object_or_404(Food, pk=food_id)

    context = {
        'food': food
    }

    return render(request, 'products/food_details.html', context)

