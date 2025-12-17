from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

@login_required
def post_list(request):
    posts = Post.objects.all()

    q = request.GET.get("q")
    if q:
        posts = posts.filter(
            Q(title__icontains=q) |
            Q(body__icontains=q) |
            Q(team__icontains=q) |
            Q(author__username__icontains=q)
        )

    return render(request, "handover/post_list.html", {"posts": posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "handover/post_detail.html", {"post": post})