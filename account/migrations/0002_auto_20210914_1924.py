# Generated by Django 2.2 on 2021-09-14 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_bloger',
            new_name='is_owner',
        ),
    ]