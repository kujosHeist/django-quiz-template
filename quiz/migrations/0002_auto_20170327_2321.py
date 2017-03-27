# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.ForeignKey(null=True, to='quiz.Answer'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=100),
        ),
    ]
