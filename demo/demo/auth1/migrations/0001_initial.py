# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 06:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=200)),
                ('no_of_employees', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('join_date', models.DateTimeField(verbose_name='date joined')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth1.Department')),
            ],
        ),
    ]
