from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from shop.models import Product, Category
from cart.forms import QuantityForm

# Helper function for pagination
def paginat(request, list_objects):
	p = Paginator(list_objects, 4)  # Show 4 items per page
	page_number = request.GET.get('page')
	try:
		page_obj = p.get_page(page_number)
	except PageNotAnInteger:  # If page is not an integer, show the first page
		page_obj = p.page(1)
	except EmptyPage:  # If page is out of range, show the last page
		page_obj = p.page(p.num_pages)
	return page_obj


# Home page view, shows all available products
def home_page(request):
	products = Product.objects.filter(quantity__gt=0)  # Only show products with quantity > 0

	# Pagination
	context = {'products': paginat(request, products)}
	return render(request, 'home_page.html', context)


# Product detail view, shows details of a single product
def product_detail(request, slug):
	form = QuantityForm()  # Form for quantity input
	product = get_object_or_404(Product, slug=slug)  # Get the product by slug
	related_products = Product.objects.filter(category=product.category).all()[:5]  # Get related products
	context = {
		'title': product.title,
		'product': product,
		'form': form,
		'favorites': 'favorites',
		'related_products': related_products
	}

	# Check if the product is in the user's favorites
	if request.user.likes.filter(id=product.id).first():
		context['favorites'] = 'remove'  # If in favorites, allow removing it
	return render(request, 'product_detail.html', context)


# Add a product to the user's favorites
@login_required
def add_to_favorites(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	request.user.likes.add(product)  # Add the product to favorites
	return redirect('shop:product_detail', slug=product.slug)


# Remove a product from the user's favorites
@login_required
def remove_from_favorites(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	request.user.likes.remove(product)  # Remove the product from favorites
	return redirect('shop:favorites')


# View that shows the user's favorite products
@login_required
def favorites(request):
	products = request.user.likes.all()  # Get all products in the user's favorites
	context = {'title': 'Favorites', 'products': products}
	return render(request, 'favorites.html', context)


# Search for products by title
def search(request):
	query = request.GET.get('q')  # Get the search query from the request
	products = Product.objects.filter(title__icontains=query).all()  # Search for products containing the query
	context = {'products': paginat(request, products)}  # Pagination
	return render(request, 'home_page.html', context)


# Filter products by category and include products from sub-categories
def filter_by_category(request, slug):
	"""Filtering by category and subcategories with the ability to sort by price."""
	result = []

	# Get the category by slug
	category = Category.objects.filter(slug=slug).first()

	# If category is not found, show an error page
	if not category:
		return render(request, 'error_page.html', {'message': f'Category "{slug}" not found.'})

	# Add products of the current category
	result.extend(Product.objects.filter(category=category))

	# If the category is not a sub-category, add products from its sub-categories
	if not category.is_sub:
		sub_categories = category.sub_categories.all()
		for sub_category in sub_categories:
			result.extend(Product.objects.filter(category=sub_category))

	# Call the filter_by_price method to sort the filtered products by price
	return filter_by_price(request, products=result)


# Sort products by price (ascending or descending)
def filter_by_price(request, products=None):
	"""Sorts products by price (ascending or descending). If filtered products are transferred, sorts them by price."""

	# Get the sort order parameter (ascending by default)
	sort_order = request.GET.get('sort', 'asc')

	# If sort order is invalid, default to ascending
	if sort_order not in ['asc', 'desc']:
		sort_order = 'asc'

	# Sort products based on the order (ascending or descending)
	if products:
		if sort_order == 'desc':
			products.sort(key=lambda x: x.price, reverse=True)  # Sort in descending order
		else:
			products.sort(key=lambda x: x.price)  # Sort in ascending order
	else:
		# If no products are provided, sort all products
		if sort_order == 'desc':
			products = Product.objects.all().order_by('-price')  # Sort by descending price
		else:
			products = Product.objects.all().order_by('price')  # Sort by ascending price

	# Pagination
	context = {
		'products': paginat(request, products),
		'sort_order': sort_order,
	}
	return render(request, 'home_page.html', context)


# Filter products by category and sort by price
def filter_by_price_with_category(request, category_slug):
	"""Filters products by category and price"""

	# Get the category by slug
	category = get_object_or_404(Category, slug=category_slug)

	# Get the sort order
	sort_order = request.GET.get('sort', 'asc')
	if sort_order not in ['asc', 'desc']:
		sort_order = 'asc'

	# Filter products by category and quantity > 0
	products = Product.objects.filter(category=category, quantity__gt=0)

	# Sort products by price
	if sort_order == 'desc':
		products = products.order_by('-price')
	else:
		products = products.order_by('price')

	context = {
		'products': paginat(request, products),
		'sort_order': sort_order,
		'category': category,
	}
	return render(request, 'home_page.html', context)
