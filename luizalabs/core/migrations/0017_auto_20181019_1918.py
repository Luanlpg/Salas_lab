# Generated by Django 2.1 on 2018-10-19 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20181019_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='sala',
            field=models.IntegerField(),
        ),
    ]
