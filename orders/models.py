from django.db import models  # Import Django's models module to define database models

# Import the User model from the accounts app
from accounts.models import User
# Import the Product model from the shop app
from shop.models import Product


# Define the Order model
class Order(models.Model):
    # Establish a foreign key relationship with the User model (one-to-many relationship)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')

    # Automatically record the date and time when the order is created
    created = models.DateTimeField(auto_now_add=True)

    # Automatically update the date and time whenever the order is updated
    updated = models.DateTimeField(auto_now=True)

    # Status of the order (e.g., whether the order is completed or not)
    status = models.BooleanField(default=False)

    class Meta:
        # Define the default ordering of the orders, ordered by creation date (most recent first)
        ordering = ('-created',)

    def __str__(self):
        # Define how the order is represented as a string (e.g., "John Doe - order id: 1")
        return f"{self.user.full_name} - order id: {self.id}"

    @property
    def get_total_price(self):
        # Calculate the total price of all items in the order
        total = sum(item.get_cost() for item in self.items.all())  # Sum the cost of each order item
        return total


# Define the OrderItem model (to represent each product in an order)
class OrderItem(models.Model):
    # Foreign key relationship with the Order model (many-to-one relationship)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

    # Foreign key relationship with the Product model (many-to-one relationship)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')

    # Price of the product in the order
    price = models.IntegerField()

    # Quantity of the product in the order
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        # Return a string representation of the order item (order item ID)
        return str(self.id)

    def get_cost(self):
        # Calculate the cost of the product in this order item
        return self.price * self.quantity  # Price multiplied by quantity
