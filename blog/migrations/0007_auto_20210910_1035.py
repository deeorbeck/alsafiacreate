# Generated by Django 3.1.7 on 2021-09-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=13, verbose_name='Telefon raqam'),
        ),
    ]
