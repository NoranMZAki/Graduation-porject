# Generated by Django 4.0.2 on 2022-06-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0017_alter_property_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='SQFT_lot',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True),
        ),
    ]
