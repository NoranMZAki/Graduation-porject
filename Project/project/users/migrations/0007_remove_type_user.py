# Generated by Django 4.0.2 on 2022-06-01 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_roles_type_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='user',
        ),
    ]
