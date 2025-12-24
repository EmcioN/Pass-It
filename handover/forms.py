from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "team", "shift", "date_for", "status", "image"]
        widgets = {
            "date_for": forms.DateInput(attrs={"type": "date"}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body", "image"]