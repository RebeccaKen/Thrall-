# Generated by Django 3.2.19 on 2023-07-11 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
