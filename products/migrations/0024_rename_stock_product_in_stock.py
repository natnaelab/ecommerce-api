# Generated by Django 5.0.6 on 2024-05-31 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_product_created_at_product_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='in_stock',
        ),
    ]
