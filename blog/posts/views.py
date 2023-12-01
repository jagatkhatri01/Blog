from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "home/index.html", context = context)