from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


class CategoryAdmin(TranslationAdmin):
    list_display = ('name',)
    list_filter = ('name',)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class ProductAdmin(TranslationAdmin):
    list_display = ('category', 'name', 'brand', 'price', 'stock', 'unit', 'created_at')
    list_filter = ('category', 'brand', 'created_at')
    search_fields = ('name', 'brand')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
