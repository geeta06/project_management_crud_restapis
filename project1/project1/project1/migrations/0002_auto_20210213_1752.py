# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2021-02-13 17:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='text',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='date',
            new_name='duration',
        ),
        migrations.RemoveField(
            model_name='project',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='task',
            name='text',
        ),
        migrations.AddField(
            model_name='project',
            name='avtar',
            field=models.ImageField(default=datetime.datetime(2021, 2, 13, 17, 52, 29, 320455, tzinfo=utc), upload_to=b'pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(default=datetime.datetime(2021, 2, 13, 17, 52, 39, 200912, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(blank=True),
        ),
    ]