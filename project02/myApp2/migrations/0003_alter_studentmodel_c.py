# Generated by Django 4.2.21 on 2025-05-19 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp2', '0002_studentmodel_delete_abcmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='c',
            field=models.IntegerField(choices=[(2020, 'двадцатый'), (2021, 'двадцать первый'), (2022, 'двадцать второй'), (2023, 'двадцать третий'), (2024, 'двадцать четвертый')], default=3, verbose_name='Год поступления'),
        ),
    ]
