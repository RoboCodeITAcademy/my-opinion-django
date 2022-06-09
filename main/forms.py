from django import forms
from .models import Post
from django.utils.text import slugify


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "body", "tag", "emoji"]
        exclude = ["author"]

    # def save(self, request):
    #     self.author = request.user
    #     self.save()
