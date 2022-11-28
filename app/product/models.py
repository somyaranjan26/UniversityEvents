from django.db import models

from app.category.models import Category
from app.location.models import Location

def dynamicImagePath(instance, filename):
    category = str(instance.category).lower()
    
    return 'images/products/{0}/{1}'.format(
        category,
        filename
    )

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    total_stock = models.IntegerField()
    current_holding = models.IntegerField()
    image = models.ImageField(upload_to=dynamicImagePath, default="images/products/default.jpeg", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name


