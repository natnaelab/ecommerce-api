# Generated by Django 5.0.6 on 2024-05-31 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.customuser',),
        ),
        migrations.CreateModel(
            name='Manager',
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
