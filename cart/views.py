from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from cart.utils.cart import Cart
from .forms import QuantityForm
from shop.models import Product

# View to add a product to the cart
@login_required
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    # Get the available quantity of the product in stock
    available_quantity = product.quantity

    # Create a form to handle quantity input and validate
    form = QuantityForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        quantity_to_add = data['quantity']

        # Check if the requested quantity exceeds the available stock
        if quantity_to_add > available_quantity:
            messages.error(request, f"We don't have that much product :(")
        else:
            # Add the product to the cart if the quantity is valid
            cart.add(product=product, quantity=quantity_to_add)
            messages.success(request, 'Added to your cart!', 'info')

    return redirect('shop:product_detail', slug=product.slug)


# View to show the contents of the cart
@login_required
def show_cart(request):
    cart = Cart(request)
    context = {'title': 'Cart', 'cart': cart}
    return render(request, 'cart.html', context)


# View to remove a product from the cart
@login_required
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:show_cart')
