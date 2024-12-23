from django.contrib import admin
from .model import Product, Supplier ,inventory

# Register your models here.
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Inventory)
