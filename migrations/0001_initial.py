# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import froala_editor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FroalaAudio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('filename', models.CharField(default=None, max_length=250)),
                ('audio', models.FileField(upload_to=froala_editor.models.audio_upload_to, verbose_name=b'\xe9\x9f\xb3\xe9\xa2\x91')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'froala_audio',
            },
        ),
        migrations.CreateModel(
            name='FroalaImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('filename', models.CharField(default=None, max_length=250)),
                ('image', models.ImageField(upload_to=froala_editor.models.image_upload_to, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'froala_images',
            },
        ),
        migrations.CreateModel(
            name='FroalaSheet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('filename', models.CharField(default=None, max_length=250)),
                ('sheet', models.FileField(upload_to=froala_editor.models.sheet_upload_to, verbose_name=b'\xe4\xb9\x90\xe8\xb0\xb1')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'froala_sheet',
            },
        ),
        migrations.CreateModel(
            name='FroalaVideo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('filename', models.CharField(default=None, max_length=250)),
                ('video', models.FileField(upload_to=froala_editor.models.video_upload_to, verbose_name=b'\xe9\x9f\xb3\xe9\xa2\x91')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'froala_video',
            },
        ),
    ]