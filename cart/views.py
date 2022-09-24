from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):
    """ A view to display the shopping cart. """

    return render(request, 'cart/cart.html')


def add_wine(request, wine_id):
    """ A view to add a quantity of the selected wine to the shopping cart. """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if wine_id in list(cart.keys()):
        cart[wine_id] += quantity
    else:
        cart[wine_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def add_food(request, food_id):
    """ A view to add a quantity of the selected food to the shopping cart. """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if food_id in list(cart.keys()):
        cart[food_id] += quantity
    else:
        cart[food_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_wine_quantity(request, wine_id):
    """
    A view to adjust the quantity of the selected wine
    within the shopping cart.
    """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[wine_id] = quantity

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def adjust_food_quantity(request, food_id):
    """
    A view to adjust the quantity of the selected food
    within the shopping cart.
    """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[food_id] = quantity

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_wine(request, wine_id):
    """ A view to remove the selected wine from the shopping cart. """

    try:
        cart = request.session.get('cart', {})

        cart.pop(wine_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)


def remove_food(request, food_id):
    """ A view to remove the selected food from the shopping cart. """

    try:
        cart = request.session.get('cart', {})

        cart.pop(food_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
