from django.urls import path

from .views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registierung/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="userprofile/login.html"), name="login"),
    path('logut/', auth_views.LogoutView.as_view(), name='logout'),

    path('passwort-vergessen/',
         auth_views.PasswordResetView.as_view(template_name="userprofile/password_reset_form.html"),
         name="password_reset_form"),
    path('passwort-vergessen/gesendet',
         auth_views.PasswordResetDoneView.as_view(template_name="userprofile/password_reset_done.html"),
         name="password_reset_done"),
    path('passwort-vergessen/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="userprofile/password_reset_confirm.html"),
         name="password_reset_confirm"),  # uib64 = user id encoded! + token
    path('passwort-vergessen/erfolgreich',
         auth_views.PasswordResetCompleteView.as_view(template_name="userprofile/password_reset_complete.html"),
         name="password_reset_complete"),
]
