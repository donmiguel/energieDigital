# Generated by Django 2.1.1 on 2018-09-17 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartGenerator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='start',
            field=models.FloatField(verbose_name='Start'),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='stop',
            field=models.FloatField(verbose_name='Stop'),
        ),
    ]
