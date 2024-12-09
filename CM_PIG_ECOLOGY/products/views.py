from django.shortcuts import render
from django.views import generic
from .models import Product 
from django.views.generic import TemplateView

class ProductListView(generic.ListView):
    model=Product
    template_name="products/list_product.html"
    context_object_name="products"

# Definir la vista utilizando TemplateView
