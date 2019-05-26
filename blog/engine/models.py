from django.db import models
from django.shortcuts import reverse

class Post(models.Model):
    slug = models.SlugField("Slug of post", max_length=15)
    title = models.CharField("Title of post", max_length=40)
    body = models.CharField("Text of post", max_length=3000)
    date = models.DateTimeField("Date", auto_now_add=True)


    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"slug": self.slug})
    


    def __str__(self):
        return "slug: {}, title: {}, text: {}, date: {}".format(self.slug, self.title, self.text, self.date)


class Tag(models.Model):
    slug = models.SlugField("Slug of post", max_length=15)
    title = models.CharField("Title of post", max_length=40)
    post = models.ManyToManyField(Post)
    date = models.DateTimeField("Date", auto_now_add=True)
    
    def __str__(self):
        return "slug: {}, title: {}, post: {}, date: {}".format(self.slug, self.title, self.post, self.date)