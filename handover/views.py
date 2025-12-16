from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, "handover/post_list.html", {"posts": posts})