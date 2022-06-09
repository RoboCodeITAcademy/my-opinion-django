from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import TemplateView, ListView
from .models import Profile, Post
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


class ProfileEditView(UpdateView):
    template_name = 'account/profile_edit.html'
    model = Profile
    # fields = "__all__"
    fields = ["name", "surname", "age", "avatar", "address", "bio", "gender"]
    # exclude = "user"
    success_url = reverse_lazy("main:profile")
