from django.contrib import admin
from products.models import ProductCategory, Product


@admin.register(ProductCategory)
class ModelNameAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ModelNameAdmin(admin.ModelAdmin):
    pass
