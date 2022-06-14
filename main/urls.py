from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("add/", views.create_post, name="add"),

    # PROFILE
    path("profile/", views.profile, name="profile"),
    path("profile/<str:user_name>/", views.other_profile, name="other_profile"),
    path("profile/edit/<pk>/", views.ProfileEditView.as_view(), name='profile_edit'),
    path("posts/", views.user_posts, name="user_posts"),
    path("detail/<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("delete/<pk>/", views.DeletePostView.as_view(), name="delete"),
    path("edit/<int:pk>/", views.EditPostView.as_view(), name="edit"),
]
