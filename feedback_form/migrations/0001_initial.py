# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback_student_info',
            fields=[
                ('fs_id', models.AutoField(serialize=False, primary_key=True)),
                ('batch_id', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=10)),
                ('semester', models.IntegerField(max_length=2)),
                ('section', models.CharField(max_length=1)),
                ('feedback_session', models.IntegerField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='infrastructure_support_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('books_availability', models.IntegerField(max_length=1)),
                ('basic_requirements', models.IntegerField(max_length=1)),
                ('technological_support', models.IntegerField(max_length=1)),
                ('study_material', models.IntegerField(max_length=1)),
                ('resourse_availability', models.IntegerField(max_length=1)),
                ('cleaniliness_of_class', models.IntegerField(max_length=1)),
                ('fs_id', models.ForeignKey(to='feedback_form.feedback_student_info')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
