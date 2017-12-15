# -*- coding: utf-8 -*-
__author__ = 'bb'
__date__ = '2017/12/15 23:34'

import  xadmin
from  .models import *


class UserCommentsAdmin(object):
    list_display = ['user', 'star', 'comment_type', 'comments', 'add_time', 'commented_id']
    search_fields = ['user', 'star', 'comment_type', 'comments','commented_id']
    list_filter = ['user', 'star', 'comment_type', 'comments', 'commented_id']

xadmin.site.register(UserComments, UserCommentsAdmin)


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type']

xadmin.site.register(UserFavorite, UserFavoriteAdmin)


class UserThumbUpAdmin(object):
    list_display = ['user', 'thumb_up_id', 'add_time']
    search_fields = ['user', 'thumb_up_id']
    list_filter = ['user', 'thumb_up_id']

xadmin.site.register(UserThumbUp, UserThumbUpAdmin)
