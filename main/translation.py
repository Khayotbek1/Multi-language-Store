from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'details')