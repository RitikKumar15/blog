from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.user_Home, name='home'),
    path('dashboard', views.user_Dashboard, name='dashboard'),
    path('profile', views.user_Profile, name='profile'),
    path('delete/<int:id>', views.user_Delete, name='delete'),
    path('logout', views.user_Logout, name='logout'),
    path('login', views.user_Login, name='login'),
    path ('signup', views.user_SignUp, name='signup'),
    path ('about', views.user_About, name='about'),
]