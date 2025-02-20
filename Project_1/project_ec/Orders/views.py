from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderedItem
from Products.models import Product

# Display cart items
def show_cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj, created = Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE,
    )

    # Calculate totals
    subtotal = sum(item.product.price * item.quantity for item in cart_obj.added_items.all())
    tax = subtotal * 0.05  # 5% tax
    total = subtotal + tax

    context = {
        'cart': cart_obj,
        'subtotal': subtotal,
        'tax': tax,
        'total': total,
    }
    return render(request, 'cart.html', context)

# Add product to cart
def add_to_cart(request, pk):
    if request.method == 'POST':
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity', 1))  # Default to 1

        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE,
        )
        product = get_object_or_404(Product, pk=pk)

        # Check if item is already in the cart
        cart_item, created = OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

    return redirect('cart')

# Remove product from cart
def remove_from_cart(request, pk):
    user = request.user
    customer = user.customer_profile
    cart_obj = get_object_or_404(Order, owner=customer, order_status=Order.CART_STAGE)

    # Get the item and remove it
    item = get_object_or_404(OrderedItem, pk=pk, owner=cart_obj)
    item.delete()

    # If no items left, delete the cart
    if not cart_obj.added_items.exists():
        cart_obj.delete()

    return redirect('cart')
