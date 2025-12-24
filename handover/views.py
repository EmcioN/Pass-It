from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib import messages
from .forms import CommentForm, PostForm
from django.db.models import Q

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
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Handover created.")
            return redirect("handover:post_detail", pk=post.pk)
    else:
        form = PostForm()

    return render(request, "handover/post_form.html", {"form": form, "title": "New handover"})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.select_related("author")

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added.")
            return redirect("handover:post_detail", pk=post.pk)
    else:
        form = CommentForm()

    return render(request, "handover/post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form,
    })

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        messages.error(request, "You are not allowed to edit this handover.")
        return redirect("handover:post_detail", pk=post.pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Handover updated.")
            return redirect("handover:post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, "handover/post_form.html", {"form": form, "title": "Edit handover"})