# Generated by Django 5.0.6 on 2024-05-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_productimage_is_primary_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
