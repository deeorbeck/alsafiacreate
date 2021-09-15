# Generated by Django 3.1.7 on 2021-09-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210914_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='card_number',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Karta raqami'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='card_vendor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Karta egasi'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='Telefon raqam'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/', verbose_name='Shaxsiy Surat'),
        ),
    ]
