from django.shortcuts import render
from .models import Product


# Create your views here.

def index_view(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'shop_name': 'Доставка продуктов'
    }
    return render(request, 'products\index.html', context=context)
