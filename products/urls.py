from django.urls import path
from products.views import IndexView, ProductsListView

app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('page/<int:page>/category/<int:category_id>', ProductsListView.as_view(), name='products_by_category'),
]
