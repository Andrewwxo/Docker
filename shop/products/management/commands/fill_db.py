from django.core.management.base import BaseCommand
from products.models import Product, Kind, Wight, Price


class Command(BaseCommand):

    def handle(self, *args, **options):
        product = Product.objects.create(name='Бакалея')

        kind = Kind.objects.create(name='Молочные продукты')

