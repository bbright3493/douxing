# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from datetime import datetime


# Create your models here.


class Destination(models.Model):

    name = models.CharField(max_length=50, verbose_name=u'目的地名称')
    publish_user = models.ForeignKey()




    desc = models.CharField(max_length=300, verbose_name=u'目的地描述')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(max_length=5, choices=(('cj', '初级'),('zj','中级'),('gj','高级')), verbose_name=u'课程等级')
    learn_time = models.IntegerField(default=0, verbose_name=u'学习时长')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name=u'课程封面')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'加入时间')
    category = models.CharField(default=u'后端开发', max_length=100, verbose_name=u'课程类型')
    tag = models.CharField(default=u'', max_length=50, verbose_name=u'课程标签')
    teacher = models.ForeignKey(Teacher, verbose_name=u'授课教师', null=True, blank=True)
    youneed_know = models.CharField(default=u'', max_length=200, verbose_name=u'课程须知')
    teacher_tell = models.CharField(default=u'', max_length=200, verbose_name=u'教师告知')

    class Meta:
        verbose_name = u'目的地信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

