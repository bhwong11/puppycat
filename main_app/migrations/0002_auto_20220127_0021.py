# Generated by Django 3.1.2 on 2022-01-27 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacation',
            name='id',
        ),
        migrations.AddField(
            model_name='vacation',
            name='vaction_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
