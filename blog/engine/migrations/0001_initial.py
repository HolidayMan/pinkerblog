# Generated by Django 2.2.1 on 2019-05-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=15, verbose_name='Slug of post')),
                ('title', models.CharField(max_length=40, verbose_name='Title of post')),
                ('text', models.CharField(max_length=3000, verbose_name='Text of post')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=15, verbose_name='Slug of post')),
                ('title', models.CharField(max_length=40, verbose_name='Title of post')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('post', models.ManyToManyField(to='engine.Post')),
            ],
        ),
    ]
