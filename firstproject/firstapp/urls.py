from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('users', views.users, name='users'),
    path('form',views.form_name_view,name='form'),
]