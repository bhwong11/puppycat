# Generated by Django 3.1.2 on 2022-01-27 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20220127_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='vacation_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
