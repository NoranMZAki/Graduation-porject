# Generated by Django 4.0.2 on 2022-06-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0035_alter_property_lat_alter_property_long_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
    ]
