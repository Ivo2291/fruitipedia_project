# Generated by Django 3.2.19 on 2023-06-24 07:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruitipedia_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FruitModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('image_URL', models.URLField()),
                ('description', models.TextField()),
                ('nutrition', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
