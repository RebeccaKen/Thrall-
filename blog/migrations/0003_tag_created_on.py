# Generated by Django 3.2.19 on 2023-06-22 08:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230622_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]