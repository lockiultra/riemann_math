# Generated by Django 4.1.7 on 2023-02-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathsources', '0002_category_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(default='', upload_to='images/categories'),
        ),
    ]
