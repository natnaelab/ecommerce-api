# Generated by Django 5.0.6 on 2024-05-31 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customer_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.customuser',),
        ),
    ]