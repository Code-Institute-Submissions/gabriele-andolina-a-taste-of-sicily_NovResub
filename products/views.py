from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Category, Food
from .forms import FoodForm


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

            queries = Q(name__icontains=query) | Q(description__icontains=query)
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


def add_food_to_store(request):
    """ Add a food product to the store """
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Well done! Your new product is now in the store.')
            return redirect(reverse('add_food_to_store'))
        else:
            messages.error(request, 'Oops! Something went wrong. Please ensure the form is valid.')
    else:
        form = FoodForm()

    template = 'products/add_food_to_store.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
