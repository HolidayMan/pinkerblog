from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectEditMixin, ObjectDeleteMixin, check_permissions
from .forms import TagForm, PostForm, PostCreateForm


class PostList(View):
    def get(self, request):
        posts = Post.objects.all()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(posts, 3)
        page = paginator.page(page_num)
        return render(request, 'engine/posts_list.html', context={"page": page})


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


class PostCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = PostCreateForm
        return render(request, 'engine/post_create.html', context={'form': form})
    
    def post(self, request):
        print(request.POST)
        bound_form = PostCreateForm(request.user, request.POST)
        if bound_form.is_valid():
            post = bound_form.save()
            return redirect(post)
        return render(request, 'engine/post_create.html', context={'form': bound_form})


class TagList(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'engine/tag_list.html', context={'tags': tags})


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form = TagForm
    template = 'engine/tag_create.html'


class PostEdit(LoginRequiredMixin, View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        if check_permissions(request.user, post):
            bound_form = PostForm(instance=post)
            return render(request, 'engine/post_edit.html', context={'form': bound_form, 'post': post})
        return render(request, 'errors/forbidden.html', status=403)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        if check_permissions(request.user, post):
            bound_form = PostForm(request.POST, instance=post)
            if bound_form.is_valid():
                bound_form.save()
                return redirect(post)
            return render(request, 'engine/post_edit.html', context={'form': bound_form, 'post': post})
        return render(request, 'errors/forbidden.html', status=403)        

    

    

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    template = "engine/post_delete_form.html"
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        if check_permissions(request.user, post):
            return render(request, self.template, context={'post': post})
        return render(request, 'errors/forbidden.html')

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        if check_permissions(request.user, post):
            post.delete()
            return redirect("posts_list_url")
        return render(request, 'errors/forbidden.html')



class TagEdit(LoginRequiredMixin, ObjectEditMixin, View):
    model = Tag
    form = TagForm
    template = 'engine/tag_edit.html'
    

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = "engine/tag_delete_form.html"