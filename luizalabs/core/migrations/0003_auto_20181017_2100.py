# Generated by Django 2.1.2 on 2018-10-17 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181016_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(max_length=200)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('inicio', models.DateTimeField(auto_now_add=True)),
                ('termino', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='salas',
            name='id',
        ),
        migrations.AlterField(
            model_name='salas',
            name='numero',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='agendamentos',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Salas'),
        ),
    ]
