from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "home/index.html", context = context)

def blog_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()

        else:
            comment_form = CommentForm()

    context = {'post': post, 'comments':comments}
    return render(request, "home/blog_detail.html", context=context)
