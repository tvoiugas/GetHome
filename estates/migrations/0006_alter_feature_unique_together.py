# Generated by Django 4.0.4 on 2022-07-18 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estates', '0005_alter_feature_kind'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='feature',
            unique_together=set(),
        ),
    ]