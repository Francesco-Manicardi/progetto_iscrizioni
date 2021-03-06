# Generated by Django 3.2.4 on 2021-07-18 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('centri', '0002_alter_centro_options'),
        ('orari', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tariffa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('centri', models.ManyToManyField(to='centri.Centro')),
                ('orari', models.ManyToManyField(to='orari.Orario')),
            ],
            options={
                'verbose_name_plural': 'Tariffe',
            },
        ),
    ]
