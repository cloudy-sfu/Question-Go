# Generated by Django 3.2.4 on 2021-06-23 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0004_transaction_created_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]