# Generated by Django 5.0.1 on 2024-01-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compromisso',
            name='concluido',
            field=models.BooleanField(default=False),
        ),
    ]
