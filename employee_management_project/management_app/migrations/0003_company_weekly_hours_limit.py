# Generated by Django 2.2.7 on 2019-12-13 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_app', '0002_auto_20191213_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='weekly_hours_limit',
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
    ]
