from django.urls import path
from .views import *

urlpatterns = [   
    path('posts/list/', PostList.as_view(), name="posts_list_url"),
    path('posts/create/', PostCreate.as_view(), name="post_create_url"),
    path('user/<str:username>/posts/', UserPostsList.as_view(), name="user_posts_list_url"),
    path('posts/<str:slug>/edit/', PostEdit.as_view(), name="post_edit_url"),
    path('posts/<str:slug>/delete/', PostDelete.as_view(), name="post_delete_url"),
    path('posts/<str:slug>/', PostDetail.as_view(), name="post_detail_url"),
    path('tags/create/', TagCreate.as_view(), name="tag_create_url"),
    path('tags/<str:slug>/edit/', TagEdit.as_view(), name='tag_edit_url'),
    path('tags/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
    path('tags/list/', TagList.as_view(), name='tags_list_url'),
    path('tags/<str:slug>/', TagDetail.as_view(), name="tag_detail_url"),
]