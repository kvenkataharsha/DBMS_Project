# Generated by Django 2.2 on 2019-05-01 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filesharing', '0002_auto_20190501_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peer',
            name='file_hash',
            field=models.CharField(max_length=100),
        ),
    ]