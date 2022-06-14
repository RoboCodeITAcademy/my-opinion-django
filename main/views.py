from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from .models import Profile, Post, Followers
from .forms import AddPostForm
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = "index.html"


def create_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.author = request.user
            f.save()
            return redirect("main:user_posts")
    else:
        form = AddPostForm()
    return render(request, "post/add.html", {"form": form})


class PostDetailView(DetailView):
    model = Post
    template_name = "post/detail.html"


class DeletePostView(DeleteView):
    model = Post
    template_name = "post/delete_confirm.html"
    success_url = reverse_lazy("main:user_posts")


class EditPostView(UpdateView):
    model = Post
    fields = ['title', 'body', 'tag', 'emoji']
    template_name = "post/edit.html"
    success_url = reverse_lazy("main:user_posts")


@login_required
def user_posts(request):
    object_list = Post.objects.filter(author=request.user)
    return render(request, "post/list.html", {"object_list": object_list})


@login_required
def profile(request):
    return render(request, "account/profile.html")


@login_required
def other_profile(request, user_name):
    user = User.objects.get(username=user_name)

    return render(request, "account/profile.html", {"user": user, "status": "other"})


class ProfileEditView(UpdateView):
    template_name = 'account/profile_edit.html'
    model = Profile
    # fields = "__all__"
    fields = ["name", "surname", "age", "avatar", "address", "bio", "gender"]
    # exclude = "user"
    success_url = reverse_lazy("main:profile")


def follow_user(request, user_name):
    # following user
    user = User.objects.get(username=request.user.username)
    # print(user)
    # will be followed user
    f_user = User.objects.get(username=user_name)
    # print(f_user)
    # following user followers
    user_follower = Followers.objects.get(user=user)

    # check followers
    if f_user not in user_follower.another_user.all():
        user_follower.another_user.add(f_user)
        user_follower.save()

        print(user_follower.another_user)

        f_user.profile.followers += 1
        user.profile.follows += 1
        user.profile.save()
        f_user.profile.save()
        messages.add_message(request, messages.SUCCESS,
                             "You successfuly following this user!")
        return redirect("account:profile", user_name=user_name)
    else:
        messages.add_message(request, messages.WARNING,
                             "You followed this user!")
        return redirect("account:profile", user_name=user_name)
