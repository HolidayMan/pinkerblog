from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup_url'),
    path('profile/', Profile.as_view(), name='profile'),
]
