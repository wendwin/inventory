from django import forms
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier' 
        }

        widgets = {
            'product_id': forms.NumberInput(
                attrs={'placeholder': 'e.g 1', 'class': 'form-control'}
            ),
            'name': forms.TextInput(
                attrs={'placeholder': 'e.g shirt', 'class': 'form-control'}
            ),
            'sku': forms.TextInput(
                attrs={'placeholder': 'e.g 1', 'class': 'form-control'}
            ),
            'price': forms.NumberInput(
                attrs={'placeholder': 'e.g 1', 'class': 'form-control'}
            ),
            'quantity': forms.NumberInput(
                attrs={'placeholder': 'e.g 1', 'class': 'form-control'}
            ),
            'supplier': forms.NumberInput(
                attrs={'placeholder': 'e.g 1', 'class': 'form-control'}
            ),
        }