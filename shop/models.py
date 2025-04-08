from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


# Category model to represent product categories
class Category(models.Model):
    # Title of the category (e.g., "Electronics", "Fashion")
    title = models.CharField(max_length=200)

    # Foreign key to represent a sub-category (self-referential)
    sub_category = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        related_name='sub_categories', null=True, blank=True
    )
    # Boolean field to check if the category is a sub-category
    is_sub = models.BooleanField(default=False)

    # Slug field to generate SEO-friendly URL
    slug = models.SlugField(max_length=200, unique=True)

    # String representation of the Category object
    def __str__(self):
        return self.title

    # Returns the absolute URL for this category (used in reverse URL resolution)
    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'slug':self.slug})

    # Automatically generate the slug based on the category title
    def save(self, *args, **kwargs): # Overriding save method
        self.slug = slugify(self.title)  # Generate slug from title
        return super().save(*args, **kwargs)  # Call the original save method to save the object


# Product model to represent individual products
class Product(models.Model):
    # Foreign key to associate the product with a category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    # Image field to upload product images
    image = models.ImageField(upload_to='products')

    # Title of the product
    title = models.CharField(max_length=250)

    # Description field for the product
    description = models.TextField()

    # Price of the product (stored as integer, representing cents/dollars)
    price = models.IntegerField()

    # Date when the product was created
    date_created = models.DateTimeField(auto_now_add=True)

    # Slug field for SEO-friendly URLs for products
    slug = models.SlugField(unique=True)

    # Quantity of the product in stock
    quantity = models.IntegerField(default=0)

    # Meta class to define ordering by date created (most recent first)
    class Meta:
        ordering = ('-date_created',)

    # String representation of the Product object (used in Django admin, shell, etc.)
    def __str__(self):
        return self.slug

    # Returns the absolute URL for this product
    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'slug':self.slug})

    # Automatically generate the slug based on the product title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # Generate slug from title
        return super().save(*args, **kwargs)  # Call the original save method to save the object
