# Generated by Django 4.0.6 on 2022-07-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estates', '0004_create_extensions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AddField(
            model_name='estate',
            name='latitude',
            field=models.FloatField(null=True, verbose_name='Координаты восточной широты'),
        ),
        migrations.AddField(
            model_name='estate',
            name='longitude',
            field=models.FloatField(null=True, verbose_name='Координаты северной долготы'),
        ),
    ]
