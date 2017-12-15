# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from user_manage.models import UserProfile


# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'目的地名称')
    publish_user = models.ForeignKey(UserProfile, verbose_name=u'发布者', null=True, blank=True)
    desc = models.CharField(max_length=600, verbose_name=u'目的地介绍')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name=u'发布时间')
    lat = models.CharField(max_length=15, verbose_name=u'纬度', )
    lng = models.CharField(max_length=15, verbose_name=u'经度', )
    custom = models.CharField(max_length=600, verbose_name=u'风俗习惯')
    festival = models.CharField(max_length=600, verbose_name=u'节日庆典')
    religion = models.CharField(max_length=600, verbose_name=u'宗教活动')
    address = models.CharField(verbose_name=u'地址信息', null=True, max_length=100 )
    contact_name = models.CharField(max_length=50, verbose_name=u'联系人姓名', null=True, blank=True)
    contact_mobile = models.CharField(max_length=11, verbose_name=u'联系人电话', null=True, blank=True)
    nearby_destination = models.ForeignKey('self', verbose_name=u'附近的目的地', null=True, blank=True)

    class Meta:
        verbose_name = u'目的地信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class TagInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'标签名称')
    type = models.IntegerField(choices=((1, u"通用标签"), (2,  u"特色标签")), default=1, verbose_name=u"标签类型")
    desc = models.CharField(max_length=600, verbose_name=u'标签内容', null=True, blank=True)
    second_tag = models.ManyToManyField('SecondTagInfo', verbose_name=u'二级标签', null=True, blank=True)

    class Meta:
        verbose_name = u'一级标签信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class SecondTagInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'标签名称')
    type = models.IntegerField(choices=((1, u"通用标签"), (2,  u"特色标签")), default=1, verbose_name=u"标签类型")
    desc = models.CharField(max_length=600, verbose_name=u'标签内容', null=True, blank=True)
    third_tag = models.ManyToManyField('ThirdTagInfo', verbose_name=u'三级标签', null=True, blank=True)

    class Meta:
        verbose_name = u'二级标签信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class ThirdTagInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'标签名称')
    type = models.IntegerField(choices=((1, u"通用标签"), (2,  u"特色标签")), default=1, verbose_name=u"标签类型")
    desc = models.CharField(max_length=600, verbose_name=u'标签内容', null=True, blank=True)
    fourth_tag = models.ManyToManyField('FourthTagInfo', verbose_name=u'四级标签', null=True, blank=True)
    class Meta:
        verbose_name = u'三级标签信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class FourthTagInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'标签名称')
    type = models.IntegerField(choices=((1, u"通用标签"), (2,  u"特色标签")), default=1, verbose_name=u"标签类型")
    desc = models.CharField(max_length=600, verbose_name=u'标签内容', null=True, blank=True)
    fifth_tag = models.ManyToManyField('FifthTagInfo', verbose_name=u'五级标签', null=True, blank=True)

    class Meta:
        verbose_name = u'四级标签信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class FifthTagInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'标签名称')
    type = models.IntegerField(choices=((1, u"通用标签"), (2,  u"特色标签")), default=1, verbose_name=u"标签类型")
    desc = models.CharField(max_length=600, verbose_name=u'标签内容', null=True, blank=True)

    class Meta:
        verbose_name = u'五级标签信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class TagDestination(models.Model):
    tag = models.ForeignKey(TagInfo, verbose_name=u'标签信息', null=True, blank=True)
    destination = models.ForeignKey(Destination, verbose_name=u'目的地信息', null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'目的地标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class ImageInfo(models.Model):
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"图片", max_length=100)
    add_id = models.IntegerField(default=0, verbose_name=u"使用图片对象id")
    image_type = models.IntegerField(choices=((1, u"目的地图片"), (2, u"服务图片"), (3, u"活动图片")), default=1, verbose_name=u"图片类型")

    class Meta:
        verbose_name = u'图片信息'
        verbose_name_plural = verbose_name
