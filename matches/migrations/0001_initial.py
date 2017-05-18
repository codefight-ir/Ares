# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
        ('robots', '0001_initial'),
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(null=True, verbose_name='date')),
                ('robot1_score', models.FloatField(default=0)),
                ('robot2_score', models.FloatField(default=0)),
                ('log', models.TextField(null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='games.Game')),
                ('league', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='leagues.League')),
                ('robot1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches1', to='robots.Robot')),
                ('robot2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches2', to='robots.Robot')),
            ],
        ),
    ]
