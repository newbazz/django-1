# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 06:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0004_auto_20171129_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCQProxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[(b'MA', b'Mathematics'), (b'CH', b'Chemistry'), (b'PH', b'Physics'), (b'GE', b'General Studies')], default=b'MA', max_length=2)),
                ('attempted', models.BooleanField(default=False)),
                ('answer', models.CharField(choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D'), (b'E', b'E')], default=b'N', max_length=1)),
                ('mark_obtained', models.IntegerField(default=0)),
                ('MCQparent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.MCQ')),
            ],
        ),
        migrations.CreateModel(
            name='TestProxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.TimeField(null=True)),
                ('updated_at', models.TimeField(auto_now=True)),
                ('MCQProxy', models.ManyToManyField(to='polls.MCQProxy')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]