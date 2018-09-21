from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    groupname = serializers.CharField(source='get_group_name')
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'pic', 'groupname')
