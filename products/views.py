from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Category, Food, Pairing
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
    pairings = food.pairings.all()

    context = {
        'food': food,
        'pairings': pairings,

    }

    return render(request, 'products/food_details.html', context)


@login_required
def add_food_to_store(request):
    """ A view to add a food item to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            food = form.save()
            messages.success(request, f'Well done! Your new product "{ food.name }" is now in the store.')
            return redirect(reverse('food_details', args=[food.id]))
        else:
            messages.error(request, 'Oops! Something went wrong. Please ensure the form is valid.')
    else:
        form = FoodForm()

    template = 'products/add_food_to_store.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_food_in_store(request, food_id):
    """ A view to edit a food item present in the store. """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    food = get_object_or_404(Food, pk=food_id)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, f'Great! You have successfully edited your "{food.name}" product.')
            return redirect(reverse('food_details', args=[food.id]))
        else:
            messages.error(request, 'Oops! Something went wrong. Please ensure the form is valid.')
    else:
        form = FoodForm(instance=food)
        messages.info(request, f'You are editing your "{food.name}" product.')

    template = 'products/edit_food_in_store.html'
    context = {
        'form': form,
        'food': food,
    }

    return render(request, template, context)


@login_required
def delete_food_from_store(request, food_id):
    """ A view to delete a food item from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    food = get_object_or_404(Food, pk=food_id)
    food.delete()
    messages.success(request, f'The "{ food.name }" product has been successfully deleted!')
    return redirect(reverse('all_products'))
