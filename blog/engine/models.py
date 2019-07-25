from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from .utils import Englishficator


def gen_slug(s, slug=None):
    eng = Englishficator()
    return_slug = slugify(eng(s if not slug else slug))
    if slug:
        return return_slug
    else:
        return return_slug + str(int(time()))


class Post(models.Model):
    slug = models.SlugField("Slug of post", max_length=50, blank=True, unique=True)
    title = models.CharField("Title of post", max_length=40)
    body = models.CharField("Text of post", max_length=3000)
    tags = models.ManyToManyField("Tag", blank=True, related_name="posts")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author", verbose_name="Author of post", blank=False)
    date = models.DateTimeField("Date", auto_now_add=True)


    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"slug": self.slug})
    

    def get_edit_url(self):
        return reverse("post_edit_url", kwargs={"slug": self.slug})


    def get_delete_url(self):
        return reverse("post_delete_url", kwargs={"slug": self.slug})


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title, self.slug)
            if self.slug in [post.slug for post in Post.objects.all()]:
                self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-date']
        permissions = (("can_edit", "Edit post"), ("can_create", "Create post"), ("can_delete", "Delete post"))


class Tag(models.Model):
    slug = models.SlugField("Slug of tag", max_length=50, unique=True)
    title = models.CharField("Title of tag", max_length=40)
    date = models.DateTimeField("Date", auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse("tag_detail_url", kwargs={"slug": self.slug})


    def get_edit_url(self):
        return reverse("tag_edit_url", kwargs={"slug": self.slug})


    def get_delete_url(self):
        return reverse("tag_delete_url", kwargs={"slug": self.slug})


    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-date']
