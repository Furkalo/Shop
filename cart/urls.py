from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    # URL for adding a product to the cart, the product ID is passed as a URL parameter
    path('add/<product_id>/', views.add_to_cart, name='add_to_cart'),

    # URL for removing a product from the cart, the product ID is passed as a URL parameter
    path('remove/<product_id>/', views.remove_from_cart, name='remove_from_cart'),

    # URL to display the contents of the cart
    path('list/', views.show_cart, name='show_cart'),
]
