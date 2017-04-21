# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from todolistapp import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^addtask/$', views.AddTaskView.as_view(), name='addtask'),
    url(r'^edittask/(?P<list_id>\d+)/$', views.EditTaskView.as_view(), name='edittask'),
    url(r'^sortbypri/$', views.SortByPrioView.as_view(), name='sortbyprio'),
    url(r'^sortbyexp/$', views.SortByExpireView.as_view(), name='sortbyexpire'),
    url(r'^deletetask/(?P<list_id>\d+)/$', views.deletetask, name='deletetask'),
    url(r'^finishtask/(?P<list_id>\d+)/$', views.finishtask, name='finishtask'),
    url(r'^backtask/(?P<list_id>\d+)/$', views.backtask, name='backtask'),
)


urlpatterns = format_suffix_patterns(urlpatterns)
