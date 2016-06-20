# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-20 20:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0003_locus'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('occupation', models.CharField(max_length=100)),
                ('simple_bar_chart', models.CharField(choices=[('Rarely', 'Rarely(Several times a year)'), ('Occasionally', 'Occasionally(Several times a month)'), ('Frequently', 'Frequently(Several times a week)'), ('Very Frequently', 'Very Frequently(Several times a day)')], max_length=20)),
                ('complex_bar_chart', models.CharField(choices=[('Rarely', 'Rarely(Several times a year)'), ('Occasionally', 'Occasionally(Several times a month)'), ('Frequently', 'Frequently(Several times a week)'), ('Very Frequently', 'Very Frequently(Several times a day)')], max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiments.User')),
            ],
        ),
    ]