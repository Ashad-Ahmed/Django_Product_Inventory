# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render

from products.models import Product
from products.forms import ProductForm

from rest_framework import viewsets
from .serializers import ProductSerializer
from .serializers import *
from .models import *
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response 

class ProductList(ListView): 
    model = Product

    def get_queryset(self):
        return Product.objects.order_by('category')

class ProductDetail(DetailView): 
    model = Product

class ProductCreate(SuccessMessageMixin, CreateView): 
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully created!"

class ProductUpdate(SuccessMessageMixin, UpdateView): 
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully updated!"

class ProductDelete(SuccessMessageMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully deleted!"
 
# create a function
def func_view(request):

    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Product.objects.all()
         
    return render(request, "Func_View.html", context)

class ProductView(APIView):
    
    def get(self,request):
        
        category = self.request.query_params.get('category')
        subcategory_type = self.request.query_params.get('subcategory_type')

        #if both product category and product subcategory_type is queried through API
        if subcategory_type and category:
            queryset = Product.objects.filter(category__category_name =  category).filter(subcategory_type__subcategory_name =  subcategory_type)

        # If Only product category is queried
        elif category and not subcategory_type:
            queryset = Product.objects.filter(category__category_name =  category)

        # If Only product subcategory_type is queried
        elif not category and subcategory_type:
            queryset = Product.objects.filter(subcategory_type__subcategory_name =  subcategory_type)
        
        # Default case
        else:
            queryset = Product.objects.all()

        serializer = ProductSerializer(queryset , many = True)
        return Response({'data' :serializer.data})

# Use below to orde the fields in ascending/descending
# queryset = Product.objects.all().order_by('name')