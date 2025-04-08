from django.urls import path  # Import the path function to define URL patterns
from orders import views  # Import the views module from the orders app

# Define the app name for namespacing URLs
app_name = "orders"

# Define the URL patterns for the orders app
urlpatterns = [
    # URL to create a new order (maps to the 'create_order' view)
    path('create', views.create_order, name='create_order'),

    # URL to display a user's list of orders (maps to the 'user_orders' view)
    path('list', views.user_orders, name='user_orders'),

    # URL for the checkout process of a specific order, takes the order ID as a parameter (maps to the 'checkout' view)
    path('checkout/<int:order_id>', views.checkout, name='checkout'),

    # URL to simulate a fake payment for an order, takes the order ID as a parameter (maps to the 'fake_payment' view)
    path('fake-payment/<int:order_id>', views.fake_payment, name='pay_order')
]
