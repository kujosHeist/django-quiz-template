# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20170327_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='answer',
            new_name='correct_answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='choices',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='quiz.Question', null=True),
        ),
    ]
