# Generated by Django 5.1.6 on 2025-02-25 11:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0008_alter_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='owner',
        ),
    ]
