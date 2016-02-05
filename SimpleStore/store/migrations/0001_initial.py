# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=400)),
                ('last_name', models.CharField(max_length=400)),
                ('address', models.CharField(max_length=600)),
                ('city', models.CharField(max_length=400)),
                ('payment_method', models.CharField(max_length=400)),
                ('payment_data', models.TextField()),
                ('fulfilled', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=850)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('imglink', models.CharField(max_length=400)),
            ],
        ),
    ]
