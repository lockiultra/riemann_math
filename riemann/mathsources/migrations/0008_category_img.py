# Generated by Django 4.1.7 on 2023-02-25 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathsources', '0007_remove_category_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(null=True, upload_to='images/categories'),
        ),
    ]
