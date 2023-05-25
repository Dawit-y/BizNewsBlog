from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import *


def home(request, *args, **kwargs):
    post_list = Post.objects.all()

    if request.method == 'POST':
        search_term = request.POST['search']
        post_list = Post.objects.filter(
            Q(title__icontains=search_term) | Q(tag__name__icontains=search_term))
    paginator = Paginator(post_list, per_page=3)
    page_number = request.GET.get('page', 1)
    tag_list = Tag.objects.all()
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    return render(request, 'post/home.html', {'posts': posts, 'tags': tag_list})


def post_detail(request, year, month, day, post):
    post_obj = get_object_or_404(Post,
                                 slug=post,
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day)
    tag_list = Tag.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        comment = request.POST['comment']

        comment_obj = Comment.objects.create(
            writer=name,
            post=post_obj,
            text=comment
        )
        comment_obj.save()
    return render(request, 'post/single.html', {'post': post_obj, 'tags': tag_list})


def contact(request):
    return render(request, 'post/contact.html', {})
