# Generated by Django 2.1.2 on 2018-10-17 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_logs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salas',
            name='numero',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]