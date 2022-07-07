from django.urls import path

from django.contrib.auth import views as auth_views
from .views import profile, edit_Profile

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="userprofile/login.html"), name="login"),
    path('logut/', auth_views.LogoutView.as_view(), name='logout'),
    path('profil/', profile, name='profile'),
    path('profil/<int:userprofile_id>', profile, name='user_profile'),
    path('profil_bearbeiten/', edit_Profile, name='edit_profile'),
]
