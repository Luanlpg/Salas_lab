# Generated by Django 2.1 on 2018-10-19 16:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_agendamentos_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamentos',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
