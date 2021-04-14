from django.shortcuts import render
from .models import Product
from .tasks import save_products
from django.views.generic import ListView, TemplateView, DetailView, FormView


class ProductListView(ListView):
    model = Product
    template_name = 'products/index.html'


class AboutTemplateView(TemplateView):
    template_name = 'products/about.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'


def index_view(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'shop_name': 'Доставка продуктов'
    }

    if request.method == "POST":
        save_products.delay()

    return render(request, 'products/index.html', context=context)
