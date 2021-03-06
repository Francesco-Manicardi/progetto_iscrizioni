# Generated by Django 3.2.4 on 2021-07-21 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bambini', '0004_bambino_codice_fiscale'),
        ('orari', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assenza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('bambino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bambini.bambino')),
                ('orario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orari.orario')),
            ],
            options={
                'verbose_name_plural': 'Assenze',
            },
        ),
    ]
