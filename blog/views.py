from django.shortcuts import render
from .models import Post

def index(request):
    # posts = Post.objects.filter(status='published').order_by('-created_at')
    return render(request, 'index.html',)

def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})
