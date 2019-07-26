from django import forms
from engine.models import Post
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError


class UserCreateForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    repeat_password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    username.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})


    def clean_username(self):
        new_username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=new_username).exists():
            raise ValidationError("This username is already used")
        return new_username

    
    def clean_email(self):
        new_email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=new_email).exists():
            raise ValidationError("This email is already used")
        return new_email


    def clean_repeat_password(self):
        password, repeated = self.cleaned_data.get('password'), self.cleaned_data.get('repeat_password')
        if password != repeated:
            raise ValidationError("Passwords don't match")
        return repeated



    def get_post_permissions(self):
        content_type = ContentType.objects.get_for_model(Post)
        permissions = Permission.objects.filter(content_type=content_type)
        return permissions


    def save(self):
        new_user = User()
        new_user.username = self.cleaned_data['username']
        new_user.email = self.cleaned_data['email']
        new_user.password = self.cleaned_data['password']
        new_user.save()
        new_user.user_permissions.add(*self.get_post_permissions())
        new_user.save()
        return new_user