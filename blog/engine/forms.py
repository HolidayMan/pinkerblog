from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError

class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.SlugField(max_length=30)
    body = forms.CharField(widget=forms.Textarea)
    tags = forms.TypedMultipleChoiceField(choices=[(tag.slug, tag.title) for tag in Tag.objects.all()], coerce=lambda slug: Tag.objects.get(slug__iexact=slug), required=False)

    title.widget.attrs.update({'class': 'form-control'})
    slug.widget.attrs.update({'class': 'form-control'})
    body.widget.attrs.update({'class': 'form-control'})
    tags.widget.attrs.update({'class': 'form-control'})

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug can\'t be named as "create".')
        if Post.objects.filter(slug__iexact=new_slug).exists():
            raise ValidationError("Slug alredy exists.")

        return new_slug
    

    def save(self):
        new_post = Post.objects.create(
            slug=self.cleaned_data['slug'],
            title=self.cleaned_data['title'],
            body=self.cleaned_data['body']
        )
        print(self.cleaned_data['tags'])
        new_post.tags.add(*self.cleaned_data['tags'])
        return new_post



class TagCreateForm(forms.Form):
    title = forms.CharField(max_length=25)
    slug = forms.SlugField(max_length=30)

    title.widget.attrs.update({'class': 'form-control'})
    slug.widget.attrs.update({'class': 'form-control'})


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug can\'t be named as "create".')
        if Tag.objects.filter(slug__iexact=new_slug).exists():
            raise ValidationError("Slug alredy exists.")

        return new_slug


    def save(self):
        new_tag = Tag.objects.create(
            slug=self.cleaned_data['slug'],
            title=self.cleaned_data['title']
        )

        return new_tag