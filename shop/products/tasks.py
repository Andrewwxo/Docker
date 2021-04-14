from celery import shared_task
import time
from .models import Product


@shared_task
def save_products():
    time.sleep(10)
    products = Product.objects.select_related('kind', 'kind__product')
    with open('products.txt', 'w', encoding='utf-8') as f:
        for product in products:
            f.write(product.name + '\n')