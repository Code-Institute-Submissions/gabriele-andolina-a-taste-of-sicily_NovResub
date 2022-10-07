from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Category, Food


def view_products(request):
    """
    A view to display the shop's products and to handle
    sorting and search queries.
    """

    foods = Food.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            foods = foods.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Don't forget to tell us what you're looking for!")
                return redirect(reverse('all_products'))

            queries = Q(product_type__icontains=query) | Q(description__icontains=query)
            foods = foods.filter(queries)

    context = {
        'foods': foods,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def view_food_details(request, food_id):
    """
    A view to display full details for each food product.
    """

    food = get_object_or_404(Food, pk=food_id)

    context = {
        'food': food
    }

    return render(request, 'products/food_details.html', context)

