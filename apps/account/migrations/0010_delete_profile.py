# Generated by Django 5.1.6 on 2025-02-25 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_rename_user_profile_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
