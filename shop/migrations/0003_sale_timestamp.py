# Generated by Django 3.2.13 on 2023-06-06 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_sale_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
