from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.clogin),
    path('register', views.register),
    path('registeruser', views.registeruser),
    path('checkuserlogin', views.checkuserlogin),
    path('changepassword', views.changepassword),
    path('updatepassword', views.updatepassword),
    path('userlogout', views.userlogout),
    path('forgetpassword', views.forgetpassword),

     # Password reset request
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='user/password_reset_form.html'),
         name='password_reset'),

    # Password reset email sent confirmation
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
         name='password_reset_done'),

    # Link from email with uid and token
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
         name='password_reset_confirm'),

    # Password reset complete
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name='password_reset_complete'),
]