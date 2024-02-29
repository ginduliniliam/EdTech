from django.contrib import admin
from .models import Product, Author


admin.site.register(Author)
admin.site.register(Product)
