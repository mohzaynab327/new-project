from rest_framework import serializers
from.models import*

class SupplierSerializer(Serializer.ModelSerializer):
    
    class Meta:
        model=Supplier
        fields='_ _all_ _'
        
class ProductSerializer(Serializer.ModelSerializer):

    class Meta:
        model=Product
        field='_ _all_ _'

class InventorySerializer(Seralizer.ModelSerializer):

    class Meta:
        model=Inventory
        field='_ _all_ _'               