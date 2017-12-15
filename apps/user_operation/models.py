# _*_ encoding:utf-8 _*_

from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from user_manage.models import UserProfile
# Create your models here.


class UserComments(models.Model):
    "用户评论"
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    star = models.IntegerField(default=0, verbose_name=u"评价星级")
    comment_type = models.IntegerField(choices=((1, u"目的地"), (2, u"服务"), (3, u"活动")), default=1, verbose_name=u"评论类型")
    comments = models.CharField(max_length=200, verbose_name=u"评论内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    commented_id = models.IntegerField(default=0, verbose_name=u"被评论数据ID")

    class Meta:
        verbose_name = u"用户评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"被收藏数据id")
    fav_type = models.IntegerField(choices=((1,"目的地"),(2,"服务"),(3,"活动")), default=1, verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class UserThumbUp(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    thumb_up_id = models.IntegerField(default=0, verbose_name=u"被点赞图片id")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户点赞"
        verbose_name_plural = verbose_name

