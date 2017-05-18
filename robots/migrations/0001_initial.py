# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 13:19
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import robots.models
import utils.storages


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'A robot with that name already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and ./+/-/_ only.', max_length=150, unique=True, validators=[django.core.validators.RegexValidator(regex='^[\\w\\.\\+\\-]+$')], verbose_name='name')),
                ('code', models.FileField(storage=utils.storages.OverwriteStorage(), upload_to=robots.models.robot_code_dir)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='robots', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]