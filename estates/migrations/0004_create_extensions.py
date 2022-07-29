from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('estates', '0003_alter_tag_options')
    ]

    operations = [
        CreateExtension('cube'),
        CreateExtension('earthdistance')
    ]
