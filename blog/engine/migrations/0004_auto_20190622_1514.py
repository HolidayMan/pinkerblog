# Generated by Django 2.2.1 on 2019-06-22 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0003_auto_20190530_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=15, unique=True, verbose_name='Slug of post'),
        ),
    ]
