from django.contrib import admin
from .models import Category, Product, Cart

# Register your models here.
@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display=['id', 'name']
    list_display_links=['name']
    search_fields=['id', 'name']

@admin.register(Product)
class Product_Admin(admin.ModelAdmin):
    list_display=['id', 'name', 'price']
    list_display_links=['name']
    search_fields=['id', 'name']

admin.site.register(Cart)