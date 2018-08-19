# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from users.models import UserProfile


class WyArticle(models.Model):
    article_id = models.AutoField(primary_key=True, verbose_name="文章id")
    a_title = models.CharField(max_length=50, blank=True, null=True, verbose_name="文章主题")
    a_conent = models.TextField(blank=True, null=True, verbose_name="文章正文")
    a_rtime = models.DateTimeField(blank=True, null=True, verbose_name="文发表时间")
    a_ctime = models.DateTimeField(blank=True, null=True, verbose_name="修改时间")
    a_user = models.ForeignKey(UserProfile, models.DO_NOTHING, db_column='a_user', blank=True, null=True,
                               verbose_name="作者")

    class Meta:
        db_table = 'wy_article'


class WyArticleUser(models.Model):
    user_id = models.ForeignKey(UserProfile, models.DO_NOTHING, blank=True, null=True)
    article_id = models.ForeignKey(WyArticle, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'wy_article_user'


class WyComment(models.Model):
    co_id = models.IntegerField(primary_key=True, verbose_name="评论id")
    article = models.ForeignKey(WyArticle, models.DO_NOTHING, related_name='comments',blank=True, null=True, verbose_name="所属文章")
    user = models.ForeignKey(UserProfile, models.DO_NOTHING, blank=True, null=True, verbose_name="所属用户")
    co_content = models.CharField(max_length=300, blank=True, null=True, verbose_name="评论内容")
    co_time = models.DateTimeField(blank=True, null=True, verbose_name="评论时间")

    class Meta:
        db_table = 'wy_comment'
