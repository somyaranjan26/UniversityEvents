from django.contrib import admin
from .models import Category

from app.admin import appAdmin 

class CategoryAdmin(admin.ModelAdmin):
    list_display= ['name', 'description', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    list_editable = ['description']
    list_per_page = 10
    ordering = ['id']
    
appAdmin.register(Category, CategoryAdmin)
