# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-09 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ostrich', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lattitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('maintainence', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Density',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=100)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ostrich.Camera')),
            ],
        ),
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('lightid', models.CharField(max_length=32, unique=True)),
                ('lattitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broken', models.BooleanField(default=0)),
                ('sender', models.BooleanField(default=0)),
                ('status', models.CharField(max_length=100)),
                ('recieved_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('light', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ostrich.Light')),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]