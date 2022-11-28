from django.contrib import admin
from .models import Product

from app.admin import appAdmin 

class ProductAdmin(admin.ModelAdmin):
    list_display= ['name', 'description', 'location', 'total_stock', 'current_holding', 'category', 'updated_at', 'image', 'note']
    list_filter = ['category', 'location']
    search_fields = ['name', 'description']
    list_per_page = 10
    ordering = ['id']

appAdmin.register(Product, ProductAdmin)