# Generated by Django 3.1.7 on 2021-09-16 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_order_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=200, verbose_name='Mavzu')),
                ('description', models.TextField(verbose_name='Sharx')),
            ],
        ),
    ]
