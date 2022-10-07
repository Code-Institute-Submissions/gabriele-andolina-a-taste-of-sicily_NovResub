from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Food

def view_cart(request):
    """ A view to display the shopping cart. """

    return render(request, 'cart/cart.html')


def add_food(request, food_id):
    """ A view to add a quantity of the selected food to the shopping cart. """

    food = get_object_or_404(Food, pk=food_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if food_id in list(cart.keys()):
        cart[food_id] += quantity
        messages.success(request, f'Updated {food.name} quantity to {cart[food_id]}.')
    else:
        cart[food_id] = quantity
        messages.success(request, f'Added {food.name} to the cart. Enjoy!')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_food_quantity(request, food_id):
    """
    A view to adjust the quantity of the selected food
    within the shopping cart.
    """

    food = get_object_or_404(Food, pk=food_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[food_id] = quantity
        messages.success(request, f'Updated {food.name} quantity to {cart[food_id]}.')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_food(request, food_id):
    """ A view to remove the selected food from the shopping cart. """

    try:
        food = get_object_or_404(Food, pk=food_id)
        cart = request.session.get('cart', {})
        cart.pop(food_id)
        messages.success(request, f'Removed {food.name} from your cart.')

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Oops! An error occurred while removing the item: {e}')
        return HttpResponse(status=500)
