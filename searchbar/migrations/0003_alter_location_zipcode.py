# Generated by Django 4.0.5 on 2023-06-29 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchbar', '0002_remove_restaurant_items_restaurant_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='zipcode',
            field=models.CharField(max_length=255),
        ),
    ]