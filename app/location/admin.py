from django.contrib import admin
from .models import Location

from app.admin import appAdmin 

class LocationAdmin(admin.ModelAdmin):
    list_display= ['name', 'description', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    list_per_page = 10
    ordering = ['id']

appAdmin.register(Location, LocationAdmin)
