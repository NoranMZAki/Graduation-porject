# Generated by Django 4.0.2 on 2022-06-15 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0023_alter_property_lat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='long',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True),
        ),
    ]