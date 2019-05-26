from django.urls import path
from .views import *

urlpatterns = [
    path('post/<str:slug>/', PostDetail.as_view(), name="post_detail_url"),
    path('', index, name="index_url"),
    
]