# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block_content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='content',
            field=models.TextField(help_text=b'Add you *markdown* here.'),
        ),
    ]
