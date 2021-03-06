# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20160628_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='output_file',
            field=models.FileField(blank=True, upload_to=jobs.models.job_directory_path),
        ),
        migrations.AlterField(
            model_name='job',
            name='configuration_file',
            field=models.FileField(blank=True, upload_to=jobs.models.job_directory_path, verbose_name=b'Config (.xml)'),
        ),
        migrations.AlterField(
            model_name='job',
            name='input_file',
            field=models.FileField(blank=True, upload_to=jobs.models.job_directory_path, verbose_name=b'Input (.gmy)'),
        ),
    ]
