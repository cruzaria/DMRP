# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-26 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=64)),
                ('course', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]
