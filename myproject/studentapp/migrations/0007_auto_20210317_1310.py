# Generated by Django 3.1 on 2021-03-17 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0006_auto_20210317_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='teacher',
            field=models.ManyToManyField(blank=True, null=True, to='studentapp.Teacher'),
        ),
    ]
