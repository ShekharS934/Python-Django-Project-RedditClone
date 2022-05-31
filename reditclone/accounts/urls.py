from django.contrib import admin
from django.urls import path, include
from accounts import views


app_name='accounts'
urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logoutview, name='logout'),
    
]
