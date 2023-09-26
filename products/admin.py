from django.contrib import admin
from products.models import ProductCategory, Product


@admin.register(ProductCategory)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ('title',)
    search_fields = ('title', )


@admin.register(Product)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'price')
    fields = ('image', 'name', 'description', 'short_description', 'category', ('quantity', 'price'))
    ordering = ('name',)
    search_fields = ('name', )
