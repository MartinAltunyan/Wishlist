# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-29 18:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quoted_by',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='text',
        ),
    ]
