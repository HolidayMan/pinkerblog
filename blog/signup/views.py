from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.core.paginator import Paginator
from .forms import UserCreateForm

class SignUp(View):
    def get(self, request):
        form = UserCreateForm()
        return render(request, 'registration/signup.html', context={'form': form})
    
    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts_list_url')
        return render(request, 'registration/signup.html', context={'form': form})