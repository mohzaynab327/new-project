from django.db import models

# Create your models here.

from django.db import models

# Supplier Model
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price with up to 8 digits and 2 decimal places
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    supplier = models.ForeignKey(Supplier, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # You can adjust the default ordering if desired.

# Inventory Model
class Inventory(models.Model):
    product = models.ForeignKey(Product, related_name='inventory', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()  # Positive integer for quantity in stock
    location = models.CharField(max_length=200)  # The location where the product is stored
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"

    class Meta:
        ordering = ['location']  # You can adjust the default ordering if desired.
