from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profile)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Emoji)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "tag"]
    prepopulated_fields = {"slug": ("title",)}
