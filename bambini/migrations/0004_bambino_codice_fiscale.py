# Generated by Django 3.2.4 on 2021-07-16 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bambini', '0003_bambino_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bambino',
            name='codice_fiscale',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
