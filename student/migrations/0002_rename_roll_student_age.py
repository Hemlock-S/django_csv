# Generated by Django 5.0.6 on 2024-05-27 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='roll',
            new_name='age',
        ),
    ]