# Generated by Django 3.1 on 2021-03-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0009_auto_20210317_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='class_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
