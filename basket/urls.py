from django.urls import path

from basket.views import add, delete

app_name = 'basket'

urlpatterns = [
    path('add/<int:product_id>/', add, name='add'),
    path('delete/<int:product_id>/', delete, name='delete')
]
