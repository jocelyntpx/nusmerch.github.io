# Generated by Django 3.0.6 on 2020-06-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nusmerch', '0013_auto_20200612_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Shirt', 'Shirt'), ('Outerwear', 'Outerwear'), ('Bottom', 'Bottom'), ('Laptop Accessories', 'Laptop Accessories'), ('Others', 'Others')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]