# Generated by Django 3.2.19 on 2023-07-12 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20230712_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='wishlist',
        ),
    ]
