# Generated by Django 2.2.6 on 2024-01-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_book_imagepath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='imagePath',
            field=models.CharField(default='https://uruguaj.com/nn.jpeg', max_length=1000),
        ),
    ]