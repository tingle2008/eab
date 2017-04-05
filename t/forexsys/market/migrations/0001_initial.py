# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fastTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symname', models.CharField(max_length=25)),
                ('dt', models.DateTimeField()),
                ('o', models.FloatField()),
                ('l', models.FloatField()),
                ('h', models.FloatField()),
                ('c', models.FloatField()),
                ('v', models.IntegerField()),
            ],
        ),
    ]
