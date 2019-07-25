from django.contrib import admin
from .models import *

def truncate_words(string, num):
    string = string.split()
    if len(string) > num:
        return " ".join(string[:num]) + " ..."
    return " ".join(string)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("slug", "title", "display_body", "display_tags", "display_author", "date")

    def display_author(self, obj):
        return obj.author
    display_author.short_description = "Author"

    def display_body(self, obj):
        return truncate_words(obj.body, 15)
    display_body.short_description = "Body"

    def display_tags(self, obj):
        return ", ".join(tag.title for tag in obj.tags.all())
    display_tags.short_description = "Tags"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("slug", "title", "display_posts", "date")
    
    def display_posts(self, obj):
        return ", ".join(post.title for post in obj.posts.all())
    display_posts.short_description = "Realated posts"
