# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-05 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20190305_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ManyToManyField(to='gallery.Category'),
        ),
    ]
