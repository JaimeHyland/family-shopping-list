from django.contrib import admin
from .models import Shop, Category, Product, List_item


# Register your models here.
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(List_item)


