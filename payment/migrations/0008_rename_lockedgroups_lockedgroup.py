# Generated by Django 3.2.4 on 2021-07-02 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('payment', '0007_auto_20210702_2014'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LockedGroups',
            new_name='LockedGroup',
        ),
    ]