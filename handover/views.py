from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def post_list(request):
    return render(request, "handover/post_list.html")