from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .models import Post, Tag

def index(request):
    posts = list(Post.objects.all())[-5:]
    return render(request, 'engine/index.html', context={"posts": posts})


class PostDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, "engine/post_detail.html", context={"post": post})