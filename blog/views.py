from django.shortcuts import render

from .models import BlogPost


def index(request):
    latest_post_list = BlogPost.objects.all()[:3]
    context = {"latest_post_list": latest_post_list}
    return render(request, "blog/index.html", context)
