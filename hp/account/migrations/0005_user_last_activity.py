# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_blocked'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_activity',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
