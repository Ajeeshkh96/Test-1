# Generated by Django 3.2.10 on 2023-01-06 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_shop', '0003_remove_product_master_strapcolor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_master',
            name='stock',
        ),
    ]