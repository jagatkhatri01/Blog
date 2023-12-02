from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.core.paginator import Paginator


# Create your views here.
def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "home/index.html", {"page_obj": page_obj})

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


def search_query(request):
    query = request.GET.get('search')
    if query:
        result = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)

    else:
        result = []
    return render(request, "home/search_results.html", {'query':query, 'result':result })




