from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

path('forgot_password',views.forgot_password,name='forgot_password'),

    path('reset_password',auth_views.PasswordResetView.as_view
    (template_name="password_reset_form.html"),name="reset_password"),

    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view
    (template_name="password_reset_sent.html") ,name="password_reset_done"),



    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view
    (template_name="reset_password.html"),name="password_reset_confirm"),

    path('password_reset_confirm',views.password_reset_confirm,name='password_reset_confirm'),

    path('password_reset_complete',views.password_reset_complete,name='password_reset_complete'),


    path('password_reset_email',views.password_reset_email,name='password_reset_email'),

    path('password_reset_form',views.password_reset_form,name='password_reset_form'),


]
