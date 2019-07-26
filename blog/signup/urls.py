from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', SignUp.as_view(), name='signup_url'),
]
