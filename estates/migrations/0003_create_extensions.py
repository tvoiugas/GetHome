from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('estates', '0002_tag_alter_feature_unique_together_alter_estate_photo_and_more')
    ]

    operations = [
        CreateExtension('cube'),
        CreateExtension('earthdistance')
    ]
