# Generated by Django 3.2.10 on 2023-01-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('seller_id', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('strapcolor', models.CharField(max_length=100)),
                ('pic', models.CharField(max_length=500)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='seller_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=500)),
                ('addr', models.CharField(max_length=500)),
                ('pin', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=150)),
                ('c_email', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='shopping_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('price', models.FloatField()),
                ('dt', models.CharField(max_length=50)),
                ('tm', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=25)),
                ('dob', models.CharField(max_length=50)),
                ('addr', models.CharField(max_length=500)),
                ('pin', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('email', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='user_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('passwd', models.CharField(max_length=25)),
                ('u_type', models.CharField(max_length=10)),
            ],
        ),
    ]
