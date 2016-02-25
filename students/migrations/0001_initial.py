# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('short_description', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
                ('address', models.CharField(max_length=200)),
                ('skype', models.CharField(max_length=15)),
                ('courses', models.ManyToManyField(to='students.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
