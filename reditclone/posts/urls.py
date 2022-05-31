from django.contrib import admin
from django.urls import path, include
from posts import views
from django.conf.urls import url


app_name='posts'
urlpatterns = [
    path('create/',views.create, name='create'),
    url(r'^(?P<pk>[0-9]+)/upvote/',views.upvote, name='upvote'),
    url(r'^(?P<pk>[0-9]+)/downvote/',views.downvote, name='downvote'),
    url(r'^user/(?P<fk>[0-9]+)', views.userposts, name='userposts'),
    
]
