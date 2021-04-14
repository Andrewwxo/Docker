from django.contrib import admin

from .models import Product, Kind, Weight, Price

# Register your models here.
admin.site.register(Product)
admin.site.register(Kind)
admin.site.register(Weight)
admin.site.register(Price)