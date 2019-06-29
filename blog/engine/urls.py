from django.urls import path
from .views import *

urlpatterns = [
    path('post/create/', PostCreate.as_view(), name="post_create_url"),
    path('post/<str:slug>/', PostDetail.as_view(), name="post_detail_url"),
    path('tag/create/', TagCreate.as_view(), name="tag_create_url"),
    path('tag/list/', TagList.as_view(), name='tag_list_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name="tag_detail_url"),
    path('', index, name="index_url"),
]