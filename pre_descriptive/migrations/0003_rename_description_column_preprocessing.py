# Generated by Django 3.2.4 on 2021-07-19 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pre_descriptive', '0002_remove_column_y_column'),
    ]

    operations = [
        migrations.RenameField(
            model_name='column',
            old_name='description',
            new_name='preprocessing',
        ),
    ]
