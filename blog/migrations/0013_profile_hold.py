# Generated by Django 3.1.7 on 2021-09-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_profile_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hold',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Hold'),
        ),
    ]