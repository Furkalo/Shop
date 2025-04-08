from cart.utils.cart import Cart
from shop.models import Category


def return_cart(request):
    cart = len(list(Cart(request))) # Count the items in the cart
    return {'cart_count': cart} # Return the count as part of the context


def return_categories(request):
    categories = Category.objects.all()  # Get all categories from the database
    return {'categories': categories}  # Return the categories as part of the context