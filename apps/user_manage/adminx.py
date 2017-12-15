# -*- coding: utf-8 -*-
__author__ = 'bb'
__date__ = '2017/12/15 23:34'

import  xadmin
from  .models import *
from xadmin.plugins.auth import UserAdmin


class UserProfileAdmin(UserAdmin):
    list_display = ['nike_name', 'birthday', 'gender', 'destination', 'address', 'mobile', 'image']
    search_fields = ['nike_name', 'birthday', 'gender', 'destination', 'address', 'mobile', 'image']
    list_filter = ['nike_name', 'birthday', 'gender', 'destination', 'address', 'mobile', 'image']

