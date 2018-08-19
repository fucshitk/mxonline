# -*- coding: utf-8 -*-
__author__ = 'wymen'

from wy_blog import views
from django.conf.urls import url, include

urlpatterns = [
    # 文章列表
    url(r'^new_article/$', views.new_article, name='new_article'),
    url(r'^article/$', views.article_list, name='article_list'),
    url(r'^article/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
    url(r'^comment/(?P<pk>\d+)/$', views.comment, name='comment'),
    # url(r'^comment/(?P<pk>\d+)/(?P<reply_pk>\d+)/$', views.comment, name='comment'),

]
