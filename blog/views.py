from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,3)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
def post_detail(request, post):
    post = get_object_or_404(Post,slug=post,status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html',{'post':post})