from django.contrib import admin
from .models import Product, Author, Lesson, Membership


admin.site.register(Author)
admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(Membership)
