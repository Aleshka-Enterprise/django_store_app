from django.views.generic import TemplateView, ListView

from common.views import TitleMixin
from products.models import Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    title = 'Store'
    template_name = 'products/index.html'


class ProductsListView(TitleMixin, ListView):
    paginate_by = 3
    title = 'Store - Каталог'
    template_name = 'products/products.html'
    model = Product

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=self.kwargs.get('category_id')) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['category_id'] = self.kwargs.get('category_id', 0)
        context['current_page'] = self.kwargs.get('page', 1)
        return context
