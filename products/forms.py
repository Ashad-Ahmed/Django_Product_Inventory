# -*- coding: utf-8 -*-
from django import forms

from products.models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        # Uncomment if you want product description and prices also added
        #self.fields['description'].widget.attrs = {
        #    'class': 'form-control col-md-6'
        #}
        self.fields['price'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }

        self.fields['category'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

        self.fields['subcategory_type'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = Product
        fields = ('name', 'price', 'category', 'subcategory_type')