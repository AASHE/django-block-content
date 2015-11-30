# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.SlugField(unique=True)),
                ('content', models.TextField(help_text=b'Add you markdown here.')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='block',
            name='theme',
            field=models.ForeignKey(blank=True, to='block_content.Theme', null=True),
        ),
    ]
