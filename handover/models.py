from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    SHIFT_CHOICES = [
        ("DAY", "Day"),
        ("NIGHT", "Night"),
    ]

    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("IN_PROGRESS", "In progress"),
        ("DONE", "Done"),
    ]

    title = models.CharField(max_length=200)
    body = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="handover_posts")

    team = models.CharField(max_length=100, blank=True)
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES, default="DAY")
    date_for = models.DateField(help_text="Date this handover is for")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="OPEN")

    image = CloudinaryField("image", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-date_for", "-created_at"]

    def __str__(self):
        return f"{self.title} ({self.date_for})"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = CloudinaryField("image", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post_id}"