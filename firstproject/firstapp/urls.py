from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.index, name="index"),
    path('users', views.users, name='users'),
    path('form', views.form_name_view, name='form'),
    path('signup', views.signup, name="signup"),
    path('register', views.register, name='register'),
    path('login', views.user_login, name="user_login"),
    path('logout', views.user_logout, name="user_logout"),
    # CBV
    path("class", views.CBView.as_view(), name="class"),
]