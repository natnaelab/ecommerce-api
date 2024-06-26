# Generated by Django 5.0.6 on 2024-05-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_added_at_cartitem_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], db_index=True, default='pending', max_length=50),
        ),
    ]
