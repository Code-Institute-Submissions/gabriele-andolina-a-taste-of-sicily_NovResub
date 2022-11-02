from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in the cart at the moment.")
        return redirect(reverse('all_products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LqNy2I5Gia0Sdxx6UD8Es9tseJ5GphxviO8PPDdGEO1ZFOwUBGxeIv2nLFbOqmEYwaSfPjjCTGCy6SdACFAADBz00m6ZWws6X',
        'client_secret': 'test_value',
    }

    return render(request, template, context)
