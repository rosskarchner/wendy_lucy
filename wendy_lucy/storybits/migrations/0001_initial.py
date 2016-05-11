# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prompt', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='pointofinterest',
            name='scene',
            field=models.ForeignKey(to='storybits.Scene'),
        ),
        migrations.AddField(
            model_name='choice',
            name='destination',
            field=models.ForeignKey(related_name='destination', to='storybits.Scene'),
        ),
        migrations.AddField(
            model_name='choice',
            name='scene',
            field=models.ForeignKey(to='storybits.Scene'),
        ),
    ]
