from django.db import models
from django.shortcuts import reverse

class Post(models.Model):
    slug = models.SlugField("Slug of post", max_length=15)
    title = models.CharField("Title of post", max_length=40)
    body = models.CharField("Text of post", max_length=3000)
    tags = models.ManyToManyField("Tag", blank=True, related_name="posts")
    date = models.DateTimeField("Date", auto_now_add=True)


    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"slug": self.slug})
    


    def __str__(self):
        return "slug: {}, title: {}, date: {}".format(self.slug, self.title, self.date)


class Tag(models.Model):
    slug = models.SlugField("Slug of post", max_length=15, unique=True)
    title = models.CharField("Title of post", max_length=40)
    date = models.DateTimeField("Date", auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse("tag_detail_url", kwargs={"slug": self.slug})


    def __str__(self):
        return "slug: {}, title: {}, date: {}".format(self.slug, self.title, self.date)