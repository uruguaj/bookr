# Generated by Django 2.2.6 on 2024-01-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20240106_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(),
        ),
    ]