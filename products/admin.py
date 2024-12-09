from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model=Product
    list_display=['name' , 'description' , 'price']
    search_fields=['name'] # añadir buscador

admin.site.register(Product , ProductAdmin)
