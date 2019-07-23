from django.shortcuts import redirect
from django.shortcuts import reverse

def blog_redirect(request):
    return redirect('posts_list_url', permanent=True)