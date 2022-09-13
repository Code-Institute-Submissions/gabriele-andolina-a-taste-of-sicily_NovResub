from django.shortcuts import render, redirect


def view_cart(request):
    """ A view to display the shopping cart. """

    return render(request, 'cart/cart.html')


def add_wine(request, item_id):
    """ A view to add a quantity of the selected wine to the shopping cart. """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
