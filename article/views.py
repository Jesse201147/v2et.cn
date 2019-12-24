from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArticlePost, ArticleColumn
import markdown
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ArticlePostForm
from django.core.paginator import Paginator
from django.db.models import Q
from comment.models import Comment
from comment.forms import CommentForm


def article_list(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    column_id = request.GET.get('column_id')
    tag = request.GET.get('tag','')
    if request.user.is_superuser:
        article_list = ArticlePost.objects.all()
    else:
        article_list = ArticlePost.objects.filter(secret=0)

    if search:
        article_list = article_list.filter(
            Q(title__contains=search) |
            Q(body__contains=search)
        )
    else:
        search = ''

    if (column_id is not None) and column_id.isdigit():
        article_list = article_list.filter(column=column_id)

    if tag and tag != 'None':
        article_list = article_list.filter(tags__name__in=[tag])

    if order == 'total_views':
        article_list = article_list.order_by('-total_views')

    paginator = Paginator(article_list, 10)
    page = request.GET.get('page')
    context = {
        'articles': paginator.get_page(page),
        'order': order,
        'search': search,
        'tag': tag,
        'columns': ArticleColumn.objects.all(),
        'column_id':int(column_id) if column_id and column_id!='None' else None
    }
    # print(context)
    return render(request, 'article/list.html', context)


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    article.total_views += 1
    article.save(update_fields=['total_views'])
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )
    article.body = md.convert(article.body)
    comment_form = CommentForm()
    comments = Comment.objects.filter(article=id)
    context = {'article': article, 'toc': md.toc, 'comments': comments,'comment_form':comment_form}
    return render(request, 'article/article_detail.html', context)


@login_required(login_url='/userprofile/login/')
def article_create(request):
    if request.method == 'POST':
        article_post_form = ArticlePostForm(request.POST,request.FILES)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=request.user.id)
            if request.POST['column'] != 'none':
                new_article.column = ArticleColumn.objects.get(id=request.POST['column'])
            new_article.save()
            article_post_form.save_m2m()
            return redirect('article:article_list')
    else:
        article_post_form = ArticlePostForm()
        columns = ArticleColumn.objects.all()
        content = {'article': article_post_form, 'columns': columns}
        return render(request, 'article/create.html', content)


@login_required(login_url='/userprofile/login/')
def article_safe_delete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        if request.user != article.author:
            return HttpResponse("抱歉，你无权修改这篇文章。")
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许POST请求")


@login_required(login_url='/userprofile/login/')
def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    # 过滤非作者的用户
    if request.user != article.author:
        return HttpResponse("抱歉，你无权修改这篇文章。")
    if request.method == 'POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.tags = request.POST['tags']
            if request.POST['column'] != 'none':
                article.column = ArticleColumn.objects.get(id=request.POST['column'])
            else:
                article.column = None
            article.save()
            return redirect('article:article_detail', id=id)
        else:
            return HttpResponse("表单内容有误, 请重新填写")
    else:
        article_post_form = ArticlePostForm()
        columns = ArticleColumn.objects.all()
        context = {'article': article, 'article_post_form': article_post_form, 'columns': columns}
        return render(request, 'article/update.html', context)


def article_home(request):
    return redirect('article:article_list')
