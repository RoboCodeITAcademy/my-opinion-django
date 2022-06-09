
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
"""
Profile 
    name , surname ,email,avatar ,gender, age, adress,bio, follows , followers
Tag 
    name , slug
Emoji 
    name , emoji=image
Post 
     title , slug ,body ,tag ,views ,author ,emoji, up, down 
Comment 
    user , name , comment (comment reply)
Statistics 
    users , visit, posts, comments, user ranking

"""


# Create your models here.
class Profile(models.Model):
    GENDERS = (
        ("erkak", "ERKAK"),
        ("ayol", "AYOL"),
        ("nomalum", "ANIQMAS"),
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(
        default='profile_images/smile.png', upload_to='profile_images/')
    gender = models.CharField(max_length=10, choices=GENDERS, blank=True)
    age = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return f"{self.name}"


class Emoji(models.Model):
    name = models.CharField(max_length=50, blank=True)
    emoji = models.ImageField(upload_to="post/emojies/")

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    title = models.CharField(max_length=250, blank=True)
    body = models.TextField(blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, related_name='tags')
    emoji = models.ForeignKey(
        Emoji, on_delete=models.PROTECT, related_name="emojies")

    # def save(self, *args, **kwargs):
    #     super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    pass
