# Generated by Django 3.2.4 on 2021-07-19 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pre_descriptive', '0003_rename_description_column_preprocessing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='column',
            old_name='preprocessing',
            new_name='description',
        ),
    ]
