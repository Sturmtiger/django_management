# Generated by Django 2.2.7 on 2019-12-13 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management_app', '0003_company_weekly_hours_limit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_total', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('workplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_app.WorkPlace')),
            ],
        ),
    ]
