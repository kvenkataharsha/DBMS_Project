# Generated by Django 2.1.2 on 2018-11-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20181117_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('rating', models.IntegerField()),
                ('text', models.CharField(max_length=250)),
            ],
        ),
    ]