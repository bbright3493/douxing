# -*- coding: utf-8 -*-
__author__ = 'bb'
__date__ = '2017/12/15 23:34'

import  xadmin
from  .models import *
from xadmin import views


class GlobalSettings(object):
    site_title="都行后台管理系统"
    site_footer="都行"
    menu_style="accordion"
xadmin.site.register(views.CommAdminView, GlobalSettings)


class DestinationAdmin(object):
    list_display = ['name', 'publish_user', 'desc', 'lat', 'lng', 'custom', 'festival', 'religion', 'address','publish_time']
    search_fields = ['name', 'publish_user', 'desc', 'lat', 'lng', 'custom', 'festival', 'religion', 'address','publish_time']
    list_filter = ['name', 'publish_user', 'desc', 'lat', 'lng', 'custom', 'festival', 'religion', 'address','publish_time']

xadmin.site.register(Destination, DestinationAdmin)


class TagInfoAdmin(object):
    list_display = ['name', 'type', 'desc', 'second_tag']
    search_fields = ['name', 'type', 'desc', 'second_tag']
    list_filter = ['name', 'type', 'desc', 'second_tag']

xadmin.site.register(TagInfo, TagInfoAdmin)


class SecondTagInfoAdmin(object):
    list_display = ['name', 'type', 'desc', 'third_tag']
    search_fields = ['name', 'type', 'desc', 'third_tag']
    list_filter = ['name', 'type', 'desc', 'third_tag']

xadmin.site.register(SecondTagInfo, SecondTagInfoAdmin)


class ThirdTagInfoAdmin(object):
    list_display = ['name', 'type', 'desc']
    search_fields = ['name', 'type', 'desc']
    list_filter = ['name', 'type', 'desc']

xadmin.site.register(ThirdTagInfo, ThirdTagInfoAdmin)


class TagDestinationAdmin(object):
    list_display = ['tag', 'destination', 'add_time']
    search_fields = ['tag', 'destination']
    list_filter = ['tag', 'destination']

xadmin.site.register(TagDestination, TagDestinationAdmin)


class DestinationImageAdmin(object):
    list_display = ['image', 'destination', 'add_id']
    search_fields = ['image', 'destination', 'add_id']
    list_filter = ['image', 'destination', 'add_id']
    model_icon = 'fa fa-film'

xadmin.site.register(ImageInfo, DestinationImageAdmin)
