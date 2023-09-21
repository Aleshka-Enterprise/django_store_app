from django.shortcuts import render
from products.models import Product, ProductCategory


def index(request):
    return render(request, 'products/index.html', {'title': 'Store'})


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products_list': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
