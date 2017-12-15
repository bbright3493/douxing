# -*- coding: utf-8 -*-
__author__ = 'bb'
__date__ = '2017/12/15 23:34'

import  xadmin
from  .models import *


class ActivityInfoAdmin(object):
    list_display = ['name', 'desc', 'publish_time', 'destination', 'cost', 'start_time', 'end_time', 'tag']
    search_fields = ['name', 'desc', 'destination', 'cost', 'tag']
    list_filter = ['name', 'desc','destination', 'cost', 'tag']

xadmin.site.register(ActivityInfo, ActivityInfoAdmin)


class ServiceInfoAdmin(object):
    list_display = ['name', 'desc', 'publish_time', 'destination', 'cost', 'start_time', 'end_time', 'tag']
    search_fields = ['name', 'desc', 'destination', 'cost', 'tag']
    list_filter = ['name', 'desc','destination', 'cost', 'tag']

xadmin.site.register( ServiceInfo, ServiceInfoAdmin)

