# Generated by Django 4.0.6 on 2022-08-07 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
