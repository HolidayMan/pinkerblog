from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .models import Post, Tag
from .utils import DetailMixin
from .forms import TagCreateForm, PostCreateForm

def index(request):
    posts = list(Post.objects.all())[::-1]
    return render(request, 'engine/index.html', context={"posts": posts})


class PostDetail(DetailMixin, View):
    model = Post
    template = "engine/post_detail.html"


class TagDetail(DetailMixin, View):
    model = Tag
    template = "engine/tag_detail.html"


class PostCreate(View):
    def get(self, request):
        form = PostCreateForm()
        return render(request, 'engine/post_create.html', context={'form': form})


    def post(self, request):
        bound_form = PostCreateForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'engine/post_create.html', context={'form': bound_form})


class TagList(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'engine/tag_list.html', context={'tags': tags})


class TagCreate(View):
    def get(self, request):
        form = TagCreateForm()
        return render(request, 'engine/tag_create.html', context={'form': form})


    def post(self, request):
        bound_form = TagCreateForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'engine/tag_create.html', context={'form': bound_form})

