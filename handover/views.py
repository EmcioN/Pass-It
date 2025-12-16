from django.shortcuts import render

def post_list(request):
    return render(request, "handover/post_list.html")