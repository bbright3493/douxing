# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-14 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondTagInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u6807\u7b7e\u540d\u79f0')),
                ('type', models.IntegerField(choices=[(1, '\u901a\u7528\u6807\u7b7e'), (2, '\u7279\u8272\u6807\u7b7e')], default=1, verbose_name='\u6807\u7b7e\u7c7b\u578b')),
                ('desc', models.CharField(blank=True, max_length=600, null=True, verbose_name='\u6807\u7b7e\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u4e8c\u7ea7\u6807\u7b7e\u4fe1\u606f',
                'verbose_name_plural': '\u4e8c\u7ea7\u6807\u7b7e\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='ThirdTagInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u6807\u7b7e\u540d\u79f0')),
                ('type', models.IntegerField(choices=[(1, '\u901a\u7528\u6807\u7b7e'), (2, '\u7279\u8272\u6807\u7b7e')], default=1, verbose_name='\u6807\u7b7e\u7c7b\u578b')),
                ('desc', models.CharField(blank=True, max_length=600, null=True, verbose_name='\u6807\u7b7e\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u4e09\u7ea7\u6807\u7b7e\u4fe1\u606f',
                'verbose_name_plural': '\u4e09\u7ea7\u6807\u7b7e\u4fe1\u606f',
            },
        ),
        migrations.AlterModelOptions(
            name='taginfo',
            options={'verbose_name': '\u4e00\u7ea7\u6807\u7b7e\u4fe1\u606f', 'verbose_name_plural': '\u4e00\u7ea7\u6807\u7b7e\u4fe1\u606f'},
        ),
        migrations.RemoveField(
            model_name='taginfo',
            name='son_tag',
        ),
        migrations.AddField(
            model_name='secondtaginfo',
            name='third_tag',
            field=models.ManyToManyField(to='destination.ThirdTagInfo', verbose_name='\u4e09\u7ea7\u6807\u7b7e'),
        ),
        migrations.AddField(
            model_name='taginfo',
            name='second_tag',
            field=models.ManyToManyField(to='destination.SecondTagInfo', verbose_name='\u4e8c\u7ea7\u6807\u7b7e'),
        ),
    ]
