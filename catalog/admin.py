from django.contrib import admin
from catalog.models import Product, ProductGroup


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    pass
