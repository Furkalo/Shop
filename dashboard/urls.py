from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404

from shop.models import Product, Category
from accounts.models import User
from orders.models import Order, OrderItem
from .forms import AddProductForm, AddCategoryForm, EditProductForm, EditCategoryForm


# Custom function to check if the user is a manager
def is_manager(user):
    try:
        if not user.is_manager:  # Check if user has manager status
            raise Http404  # If not a manager, raise 404 error
        return True
    except:
        raise Http404  # In case of an error, raise 404 error


# View to list all products, only accessible to managers
@user_passes_test(is_manager)
@login_required
def products(request):
    products = Product.objects.all()  # Retrieve all products
    context = {'title': 'Products', 'products': products}  # Pass products to the template
    return render(request, 'products.html', context)


# View to add a new product, only accessible to managers
@user_passes_test(is_manager)
@login_required
def add_product(request):
    if request.method == 'POST':  # Check if form is submitted
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():  # If form is valid, save the product
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('dashboard:add_product')  # Redirect to add product page
    else:
        form = AddProductForm()  # Initialize empty form
    context = {'title': 'Add Product', 'form': form}
    return render(request, 'add_product.html', context)


# View to delete a product, only accessible to managers
@user_passes_test(is_manager)
@login_required
def delete_product(request, id):
    product = Product.objects.filter(id=id).delete()  # Delete the product with the given id
    messages.success(request, 'Product has been deleted!')
    return redirect('dashboard:products')  # Redirect to product listing page


# View to edit an existing product, only accessible to managers
@user_passes_test(is_manager)
@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)  # Retrieve the product, or return 404 if not found
    if request.method == 'POST':  # Check if form is submitted
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():  # If form is valid, update the product
            form.save()
            messages.success(request, 'Product has been updated')
            return redirect('dashboard:products')  # Redirect to product listing page
    else:
        form = EditProductForm(instance=product)  # Initialize form with existing product data
    context = {'title': 'Edit Product', 'form': form}
    return render(request, 'edit_product.html', context)


# View to list all categories, only accessible to managers
@user_passes_test(is_manager)
@login_required
def categories(request):
    categories = Category.objects.all()  # Retrieve all categories
    context = {'title': 'Categories', 'categories': categories}  # Pass categories to the template
    return render(request, 'categories.html', context)


# View to add a new category, only accessible to managers
@user_passes_test(is_manager)
@login_required
def add_category(request):
    if request.method == 'POST':  # Check if form is submitted
        form = AddCategoryForm(request.POST)
        if form.is_valid():  # If form is valid, save the category
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('dashboard:add_category')  # Redirect to add category page
    else:
        form = AddCategoryForm()  # Initialize empty form
    context = {'title': 'Add Category', 'form': form}
    return render(request, 'add_category.html', context)


# View to delete a category, only accessible to managers
@user_passes_test(is_manager)
@login_required
def delete_category(request, id):
    category = Category.objects.filter(id=id).delete()  # Delete the category with the given id
    messages.success(request, 'Category has been deleted!')
    return redirect('dashboard:categories')  # Redirect to category listing page


# View to edit an existing category, only accessible to managers
@user_passes_test(is_manager)
@login_required
def edit_category(request, id):
    category = get_object_or_404(Category, id=id)  # Retrieve the category, or return 404 if not found
    if request.method == 'POST':  # Check if form is submitted
        form = EditCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():  # If form is valid, update the category
            form.save()
            messages.success(request, 'Category has been updated')
            return redirect('dashboard:categories')  # Redirect to category listing page
    else:
        form = EditCategoryForm(instance=category)  # Initialize form with existing category data
    context = {'title': 'Edit Category', 'form': form}
    return render(request, 'edit_category.html', context)


# View to list all orders, only accessible to managers
@user_passes_test(is_manager)
@login_required
def orders(request):
    orders = Order.objects.all()  # Retrieve all orders
    context = {'title': 'Orders', 'orders': orders}  # Pass orders to the template
    return render(request, 'orders.html', context)


# View to display detailed order information, only accessible to managers
@user_passes_test(is_manager)
@login_required
def order_detail(request, id):
    order = Order.objects.filter(id=id).first()  # Retrieve the order with the given id
    items = OrderItem.objects.filter(order=order).all()  # Retrieve all order items for the order
    context = {'title': 'Order Detail', 'items': items, 'order': order}  # Pass order and items to the template
    return render(request, 'order_detail.html', context)
