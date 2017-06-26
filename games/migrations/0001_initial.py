# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-25 16:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import games.models
import utils.storages


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'A game with that name already exists.'}, help_text='Required. 150 characters or fewer.', max_length=150, unique=True, verbose_name='name')),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('instruction', models.TextField()),
                ('rules', models.TextField()),
                ('code', models.FileField(storage=utils.storages.CustomStorage(), upload_to=games.models.game_code_dir, validators=[django.core.validators.FileExtensionValidator(['py'])])),
            ],
        ),
    ]
