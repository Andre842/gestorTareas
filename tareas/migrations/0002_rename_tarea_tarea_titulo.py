# Generated by Django 5.0.7 on 2024-07-28 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='tarea',
            new_name='titulo',
        ),
    ]
