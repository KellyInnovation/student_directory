# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('bio', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField()),
            ],
        ),
    ]
