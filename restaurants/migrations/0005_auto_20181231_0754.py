# Generated by Django 2.1.4 on 2018-12-31 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_restaurantlocation_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurantlocation',
            old_name='user',
            new_name='owner',
        ),
    ]