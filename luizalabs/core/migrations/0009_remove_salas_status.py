# Generated by Django 2.1.2 on 2018-10-18 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20181018_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salas',
            name='status',
        ),
    ]
