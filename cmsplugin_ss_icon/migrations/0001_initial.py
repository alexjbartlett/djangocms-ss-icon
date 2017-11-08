# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-08 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_ss_icon_icon', serialize=False, to='cms.CMSPlugin')),
                ('icon', models.CharField(help_text='A font-awesome class, e.g. fa-facebook or fa-cog', max_length=255, verbose_name='Icon')),
                ('size', models.CharField(blank=True, choices=[(None, 'Standard'), ('fa-lg', 'Large'), ('fa-2x', '2x Large'), ('fa-3x', '3x Large'), ('fa-4x', '4x Large'), ('fa-5x', '5x Large')], max_length=5, null=True, verbose_name='Size')),
                ('fixed_width', models.BooleanField(default=False, verbose_name='Fixed Width')),
                ('spin', models.BooleanField(default=False, help_text='Icon will rotate smoothly.  Works well with spinner, refresh, cog', verbose_name='Spin')),
                ('pulse', models.BooleanField(default=False, help_text='Icon will rotate with 8 steps.  Works well with spinner, refresh, cog', verbose_name='Pulse')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]