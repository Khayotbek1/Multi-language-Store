# Generated by Django 5.2.4 on 2025-07-13 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='details_en',
            field=models.TextField(blank=True, null=True, verbose_name='Details'),
        ),
        migrations.AddField(
            model_name='product',
            name='details_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Details'),
        ),
        migrations.AddField(
            model_name='product',
            name='details_uz',
            field=models.TextField(blank=True, null=True, verbose_name='Details'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
    ]
