from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "team", "shift", "status", "date_for", "author", "created_at")
    list_filter = ("team", "shift", "status", "date_for")
    search_fields = ("title", "body", "team", "author__username")
    ordering = ("-date_for", "-created_at")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_at")
    search_fields = ("body", "author__username", "post__title")