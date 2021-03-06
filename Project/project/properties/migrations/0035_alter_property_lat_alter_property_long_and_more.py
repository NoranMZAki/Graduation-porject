# Generated by Django 4.0.2 on 2022-06-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0034_alter_property_bathrooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='lat',
            field=models.DecimalField(decimal_places=4, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='long',
            field=models.DecimalField(blank=0, decimal_places=3, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
    ]
