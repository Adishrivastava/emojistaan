# Generated by Django 2.2.3 on 2019-11-29 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191130_0141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofiles',
            name='specials',
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='deaf',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
