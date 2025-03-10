from datetime import date

from django.shortcuts import render
from .models import Post

# Create your views here.


def my_func(post):
    return post['date']

def starting_page(request):
    final_post = Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html",{
        "posts" : final_post
    })

def posts(request):
    all_posts = Post.objects.all()
    return render(request,"blog/all-posts.html",{
        "posts": all_posts
    })

def post_detail(request, slug):
    identified_post = Post.objects.get(slug=slug)
    return render(request, "blog/post-detail.html",{
        "post" : identified_post
    })