from django import forms

class QuantityForm(forms.Form):
    # Define an IntegerField for quantity
    quantity = forms.IntegerField(
        label='',  # No label will be displayed for this field
        min_value=1,  # Minimum quantity value is 1
        max_value=99,  # Maximum quantity value is 99
        widget=forms.NumberInput(
            attrs={'class': 'form-control mt-1', 'placeholder': 'quantity'}
        )  # Uses a number input widget with specified CSS classes and placeholder text
    )
