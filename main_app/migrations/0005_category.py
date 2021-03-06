# Generated by Django 3.1.2 on 2022-01-27 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20220127_0230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('vacations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.vacation')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
