# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-01 23:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0003_profilefeditem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileFedItem',
            new_name='ProfileFeedItem',
        ),
    ]