from shop.models import Product

# Define the session key for the cart
CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self, request):
        # Initialize the cart using the session data
        self.session = request.session
        self.cart = self.add_cart_session()

    def __iter__(self):
        # Iterate over the cart items and yield them with product details
        product_ids = self.cart.keys()  # Get all the product IDs in the cart
        products = Product.objects.filter(id__in=product_ids)  # Get products from the database using product IDs
        cart = self.cart.copy()  # Create a copy of the cart to avoid modifying the original session data

        # Attach the product details to the cart items
        for product in products:
            cart[str(product.id)]['product'] = product

        # Calculate the total price for each item and yield each item
        for item in cart.values():
            item['total_price'] = int(item['price']) * int(item['quantity'])
            yield item

    def add_cart_session(self):
        # Get the cart from the session if it exists, otherwise initialize it as an empty dictionary
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        return cart

    def add(self, product, quantity):
        # Add a product to the cart with a specified quantity
        product_id = str(product.id)

        # If the product is not in the cart, initialize it with quantity 0 and its price
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        # Update the quantity of the product in the cart
        self.cart.get(product_id)['quantity'] += quantity
        self.save()

    def remove(self, product):
        # Remove a product from the cart
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        # Mark the session as modified to save the cart data
        self.session.modified = True

    def get_total_price(self):
        # Calculate the total price of all items in the cart
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # Clear the cart from the session
        del self.session[CART_SESSION_ID]
        self.save()
