from django.contrib import admin


class AppAdmin(admin.AdminSite):
    index_title = "University Events Inventory"
    site_header = 'Rowan University'
    site_title = 'University Events Inventory'

appAdmin = AppAdmin(name='app')
