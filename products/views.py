from django.core.paginator import Paginator
from django.shortcuts import render
from products.models import Product, ProductCategory


def index(request):
    return render(request, 'products/index.html', {'title': 'Store'})


def products(request, category_id=0, page=1):
    if category_id:
        products_list = Product.objects.filter(category_id=category_id)
    else:
        products_list = Product.objects.all()

    products_paginator = Paginator(products_list, 3)

    context = {
        'title': 'Store - Каталог',
        'products_paginator': products_paginator.page(page),
        'categories': ProductCategory.objects.all(),
        'current_page': page,
        'category_id': category_id,
    }
    return render(request, 'products/products.html', context)
