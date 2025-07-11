from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'brand', 'price', 'stock', 'unit', 'created_at')
    list_filter = ('category', 'brand', 'created_at')
    search_fields = ('name', 'brand')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
