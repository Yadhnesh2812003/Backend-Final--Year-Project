# Generated by Django 4.0 on 2022-05-01 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_quicknotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quicknotes',
            name='notes_value',
            field=models.CharField(max_length=10000000),
        ),
    ]
