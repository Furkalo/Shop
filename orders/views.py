from django.shortcuts import render, redirect, get_object_or_404  # Import necessary Django functions
from django.contrib.auth.decorators import login_required  # Import the login_required decorator to restrict views to authenticated users

from django.views.decorators.http import require_POST  # (Not used here, but it can be used to enforce POST requests)
from django.utils import timezone  # Import timezone (not used directly, but useful for handling date/time)
from pyexpat.errors import messages  # Import messages for showing alerts to the user

from .models import Order, OrderItem  # Import the Order and OrderItem models from the current app
from cart.utils.cart import Cart  # Import the Cart utility to handle cart operations


# View to create an order after user is logged in
@login_required
def create_order(request):
    cart = Cart(request)  # Retrieve the user's cart

    # Create a new order for the logged-in user
    order = Order.objects.create(user=request.user)

    # Loop through each item in the cart
    for item in cart:
        product = item['product']  # Retrieve the product from the cart item
        quantity_ordered = item['quantity']  # Get the quantity of the product ordered

        # Check if the product has enough stock available
        if quantity_ordered > product.quantity:
            messages.error(request, f"Not enough stock for {product.title}.")  # Display an error message
            return redirect('cart:show_cart')  # Redirect back to the cart page if stock is insufficient

        # Create an OrderItem instance for this product and quantity
        OrderItem.objects.create(
            order=order,
            product=product,
            price=item['price'],
            quantity=quantity_ordered
        )

        # Reduce the stock quantity of the product based on the ordered quantity
        product.quantity -= quantity_ordered
        product.save()

    # Clear the cart once the order is created and items are processed
    cart.clear()

    # Redirect the user to the order payment page
    return redirect('orders:pay_order', order_id=order.id)


# View to display the checkout page for an order
@login_required
def checkout(request, order_id):
    # Get the order by its ID or return a 404 error if not found
    order = get_object_or_404(Order, id=order_id)
    # Context for rendering the checkout page
    context = {'title': 'Checkout', 'order': order}
    return render(request, 'checkout.html', context)  # Render the checkout page with the order details


# View to simulate a fake payment and update the order status
@login_required
def fake_payment(request, order_id):
    cart = Cart(request)  # Retrieve the cart to clear it after payment
    cart.clear()  # Clear the cart
    order = get_object_or_404(Order, id=order_id)  # Get the order by its ID or return a 404 error if not found
    order.status = True  # Mark the order as paid by changing its status
    order.save()  # Save the order with the updated status
    # Redirect the user to the page displaying all their orders
    return redirect('orders:user_orders')


# View to display all orders placed by the logged-in user
@login_required
def user_orders(request):
    # Retrieve all orders for the logged-in user
    orders = request.user.orders.all()
    # Context for rendering the user orders page
    context = {'title': 'Orders', 'orders': orders}
    return render(request, 'user_orders.html', context)  # Render the user orders page with the orders data

