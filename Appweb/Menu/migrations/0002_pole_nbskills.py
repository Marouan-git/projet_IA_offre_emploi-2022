# Generated by Django 3.1.5 on 2022-02-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pole',
            name='nbSkills',
            field=models.IntegerField(default=0),
        ),
    ]
