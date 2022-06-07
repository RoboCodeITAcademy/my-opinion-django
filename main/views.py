from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from .models import Profile
# Create your views here.


class HomeView(TemplateView):
    template_name = "index.html"


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
