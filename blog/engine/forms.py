from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug can\'t be named as "create".')

        return new_slug
    

class PostCreateForm(forms.Form):
    author = None

    title = forms.CharField(max_length=50)
    slug = forms.SlugField(allow_unicode=True, max_length=50, required=False)
    body = forms.CharField(widget=forms.Textarea(attrs={}))
    tags = forms.TypedMultipleChoiceField(choices=list(zip(range(len(Tag.objects.all())), [tag.title for tag in Tag.objects.all()])),
     coerce=lambda num: Tag.objects.all()[int(num)])

    title.widget.attrs.update({'class': 'form-control'})
    slug.widget.attrs.update({'class': 'form-control'})
    body.widget.attrs.update({'class': 'form-control'})
    tags.widget.attrs.update({'class': 'form-control'})


    def __init__(self, author=None, *args, **kwargs):
        self.author = author
        super().__init__(*args, **kwargs)


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug can\'t be named as "create".')
        return new_slug
    

    def save(self):
        if self.author:
            post = Post()
            post.title = self.cleaned_data['title']
            post.slug = self.cleaned_data['slug']
            post.body = self.cleaned_data['body']
            post.author = self.author
            post.save()
            post.tags.add(*self.cleaned_data['tags'])
            post.save()
            return post



class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),

        }


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug can\'t be named as "create".')
        # if Tag.objects.filter(slug__iexact=new_slug).exists():
        #     raise ValidationError("Slug alredy exists.")

        return new_slug
