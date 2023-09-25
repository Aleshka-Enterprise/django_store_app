from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from basket.models import Basket


@login_required
def add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(product=product, user=request.user)
    if basket.exists():
        basket = basket.first()
        basket.quantity += 1
        basket.save()
    else:
        Basket.objects.create(user=request.user, product=product, quantity=1)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def delete(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(product=product, user=request.user)
    if basket.exists():
        basket = basket.first()
        basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
