# -*- coding: utf-8 -*-
__author__ = 'ysir'
__date__ = '2018/8/20 22:29'

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'add_time']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'city', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_commpany', 'work_position', 'points', 'click_nums',
                    'fav_nums', 'add_time']
    search_fields = ['org__name', 'name', 'work_years', 'work_commpany', 'work_position', 'points', 'click_nums',
                     'fav_nums']
    list_filter = ['org__name', 'name', 'work_years', 'work_commpany', 'work_position', 'points', 'click_nums',
                   'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
