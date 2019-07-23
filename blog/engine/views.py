from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectEditMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm


class PostList(View):
    def get(self, request):
        posts = Post.objects.all()
        page = request.GET.get('page') if request.GET.get('page') else 1
        paginator = Paginator(posts, 3)
        return render(request, 'engine/posts_list.html', context={"page": paginator.page(page)})


class PostListAll(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'engine/posts_list_all.html', context={"posts": posts})        


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = "engine/post_detail.html"


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = "engine/tag_detail.html"


class PostCreate(ObjectCreateMixin, View):
    form = PostForm
    template = 'engine/post_create.html'

class TagList(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'engine/tag_list.html', context={'tags': tags})


class TagCreate(ObjectCreateMixin, View):
    form = TagForm
    template = 'engine/tag_create.html'


class PostEdit(ObjectEditMixin, View):
    model = Post
    form = PostForm
    template = 'engine/post_edit.html'
    

class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = "engine/post_delete_form.html"


class TagEdit(ObjectEditMixin, View):
    model = Tag
    form = TagForm
    template = 'engine/tag_edit.html'
    

class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = "engine/tag_delete_form.html"