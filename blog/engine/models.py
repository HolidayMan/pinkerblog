from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from .utils import Englishficator

def gen_slug(s):
    eng = Englishficator()
    slug = slugify(eng(s))
    return slug + str(int(time()))


class Post(models.Model):
    slug = models.SlugField("Slug of post", max_length=50, blank=True, unique=True)
    title = models.CharField("Title of post", max_length=40)
    body = models.CharField("Text of post", max_length=3000)
    tags = models.ManyToManyField("Tag", blank=True, related_name="posts")
    date = models.DateTimeField("Date", auto_now_add=True)


    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"slug": self.slug})
    

    def get_edit_url(self):
        return reverse("post_edit_url", kwargs={"slug": self.slug})


    def get_delete_url(self):
        return reverse("post_delete_url", kwargs={"slug": self.slug})


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-date']


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
