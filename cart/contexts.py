from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Wine, Food


def cart_contents(request):
    # This is the main delivery logic; however, when the time comes to allow users to complete
    # payments, this will need to be updated: customers from Italy (will have to use their address as the key discriminant)
    # will get free delivery no matter what the grand_total is, whereas the following logic will apply to
    # customers from Europe.
    
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for wine_id, quantity in cart.items():
        wine = get_object_or_404(Wine, pk=wine_id)
        total += quantity * wine.price
        product_count += quantity
        cart_items.append({
            'wine_id': wine_id,
            'quantity': quantity,
            'wine': wine,
        })

    for food_id, quantity in cart.items():
        food = get_object_or_404(Food, pk=food_id)
        total += quantity * food.price
        product_count += quantity
        cart_items.append({
            'food_id': food_id,
            'quantity': quantity,
            'food': food,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
