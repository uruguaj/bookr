# Generated by Django 2.2.6 on 2024-01-06 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20240106_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='imagePath',
        ),
    ]
