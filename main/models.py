from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('Name'),max_length=255)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    name = models.CharField(_('Name'), max_length=255)
    details = models.TextField(_('Details'), null=True, blank=True)
    brand = models.CharField(_('Brand'), max_length=255, null=True, blank=True)
    price = models.FloatField(_('Price'), null=True, blank=True)
    stock = models.FloatField(_('Stock'), null=True, blank=True)
    unit = models.CharField(_('Unit'), max_length=100)
    created_at = models.DateTimeField(_('Created_at'),auto_now_add=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name
