# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from destination.models import Destination, TagInfo


class ActivityInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'活动名称')
    desc = models.CharField(max_length=600, verbose_name=u'活动介绍')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name=u'发布时间')
    destination = models.ManyToManyField(Destination, verbose_name=u'活动目的地')
    cost = models.CharField(max_length=100, verbose_name=u'活动费用')
    start_time = models.DateTimeField(default='', verbose_name=u'开始时间')
    end_time = models.DateTimeField(default='', verbose_name=u'结束时间')
    tag = models.ManyToManyField(TagInfo, verbose_name=u'标签信息')

    class Meta:
        verbose_name = u"活动信息"
        verbose_name_plural = verbose_name


class ServiceInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'服务名称')
    desc = models.CharField(max_length=600, verbose_name=u'服务介绍')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name=u'发布时间')
    destination = models.ManyToManyField(Destination, verbose_name=u'服务目的地')
    cost = models.CharField(max_length=100, verbose_name=u'服务费用')
    start_time = models.DateTimeField(default='', verbose_name=u'开始时间')
    end_time = models.DateTimeField(default='', verbose_name=u'结束时间')
    tag = models.ManyToManyField(TagInfo, verbose_name=u'标签信息')

    class Meta:
        verbose_name = u"服务信息"
        verbose_name_plural = verbose_name

