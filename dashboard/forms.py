from django import forms
from django.forms import ModelForm

from shop.models import Product, Category


# Form for adding a new product
class AddProductForm(ModelForm):
    class Meta:
        model = Product  # Model the form is based on
        fields = ['category', 'image', 'title','description', 'price', 'quantity']  # Fields to be included in the form

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        # Assigning 'form-control' CSS class to all visible fields for styling
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


# Form for adding a new category
class AddCategoryForm(ModelForm):
    class Meta:
        model = Category  # Model the form is based on
        fields = ['title', 'sub_category', 'is_sub']  # Fields to be included in the form

    def __init__(self, *args, **kwargs):
        super(AddCategoryForm, self).__init__(*args, **kwargs)
        # Assigning 'form-check-input' class for checkbox and 'form-control' for text fields
        self.fields['is_sub'].widget.attrs['class'] = 'form-check-input'
        self.fields['sub_category'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'


# Form for editing an existing product
class EditProductForm(ModelForm):
    class Meta:
        model = Product  # Model the form is based on
        fields = ['category', 'image', 'title','description', 'price', 'quantity']  # Fields to be included in the form

    def __init__(self, *args, **kwargs):
        super(EditProductForm, self).__init__(*args, **kwargs)
        # Assigning 'form-control' CSS class to all visible fields for styling
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


# Form for editing an existing category
class EditCategoryForm(ModelForm):
    class Meta:
        model = Category  # Model the form is based on
        fields = ['title', 'sub_category', 'is_sub']  # Fields to be included in the form

    def __init__(self, *args, **kwargs):
        super(EditCategoryForm, self).__init__(*args, **kwargs)
        # Assigning 'form-control' CSS class to all visible fields for styling
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        # Customizing specific fields for styling
        self.fields['is_sub'].widget.attrs['class'] = 'form-check-input'
