from django.shortcuts import render, redirect


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
    print(request.session['cart'])
    return redirect(redirect_url)


def add_food(request, food_id):
    """ A view to add a quantity of the selected wine to the shopping cart. """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if food_id in list(cart.keys()):
        cart[food_id] += quantity
    else:
        cart[food_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
