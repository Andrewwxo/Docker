from django.core.management.base import BaseCommand
from products.models import Product, Kind, Weight, Price


class Command(BaseCommand):

    def handle(self, *args, **options):
        # product = Product.objects.create(name='Напитки')
        product = Product.objects.create(name='Молочные продукты')

        # kind = Kind.objects.create(name='Безаклкогольные напитки', product=product)

