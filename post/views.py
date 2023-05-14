from django.shortcuts import render, redirect
from post.forms import ReplyForm
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
from .models import *

def home(request, *args, **kwargs):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, per_page=3)
    page_number = request.GET.get('page', 1)
    try: 
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request, 'post/index.html', {'news': posts })

def post_detail(request, year, month, day, post):
    post_obj = get_object_or_404(Post,
                        slug=post,
                        publish__year=year,
                        publish__month=month,
                        publish__day=day)
    return render(request, 'post/single.html', {'post': post_obj})

def reply(request, pk):
    comment = Comment.objects.get(pk=pk)
    reply = comment.reply_set.all()
    form = ReplyForm()
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.writer = request.user
            instance.comment = comment
            instance.save()
            return redirect('home')    
        else:
            form = ReplyForm()
            print('failed reply')
            return redirect('home')
    context = {'reply': reply}
    return render(request, 'post/home.html', context)


