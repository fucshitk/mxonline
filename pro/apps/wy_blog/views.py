# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import View

from users.models import UserProfile
from wy_blog.models import WyArticle, WyComment
from django.db.models import Count
import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# def board_topics(request, pk):
#     # 查询Board中pk=pk，如果不存在则404错误
#     board = get_object_or_404(WyArticle, pk=pk)
#     '''
#     这⾥我们使⽤ annotate ，QuerySet将即时⽣成⼀个新的列，这个新的列，
#     将被翻译成⼀个属性，可通过topic.replies来访问，它包含了指定主题下的回复数。
#     '''
#     topics = board.a_title.order_by('-a_ctime').annotate(replies=Count('posts')-1)
#     return render(request, 'wy_blog.html', {'board': board,'topics':topics})


from django.http import HttpResponse


def hello(request):
    # return HttpResponse('<h1> 这里是学员交流的天地</h1>')
    return render(request, 'wy-blog-list.html')


# 发表新文章
# @login_required
def new_article(request):
    # article = get_object_or_404(WyArticle)
    if request.method == 'POST':
        a_title = request.POST['a_title']
        a_conent = request.POST['a_conent']

        # user = UserProfile.objects.first()
        user = request.user
        print(user,user.id)
        article = WyArticle.objects.create(
            a_title=a_title,
            a_conent=a_conent,
            a_rtime=datetime.datetime.now().strftime('%Y-%m-%d'),
            a_ctime=datetime.datetime.now().strftime('%Y-%m-%d'),
            a_user=user.id,
        )
        print('--------------', article.a_title)
        return redirect(reverse('blog:article_list'))

    return render(request, 'wy-new-article.html')


# 文章列表
def article_list(request):
    article = WyArticle.objects.all()
    context = {
        'article': article
    }
    return render(request, 'wy-article-list.html', context=context)


# 文章详情+评论列表
def article_detail(request, pk):
    article = WyArticle.objects.filter(pk=pk).first()
    commentList = article.comments.all()
    context = {
        'article': article,
        'reply_pk':request.user,
        'commentList':commentList,
    }

    return render(request, 'wy-article-detail.html', context=context)


# 评论窗口
# @login_required
def comment(request, pk):
    if request.method == 'POST':
        co_content = request.POST['co_content']

        # user = UserProfile.objects.first()
        user = request.user
        article = WyArticle.objects.filter(pk=pk).first()
        comment = WyComment.objects.create(
            article=article,
            user=user.id,
            co_content=co_content,
            co_time=datetime.datetime.now().strftime('%Y-%m-%d'),
            # co_time='2018-08-14 00:00:00',
        )

        print('--------------', comment.co_content)

    return redirect(reverse('blog:article_detail',args=(pk,)))


