from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_blog_post, name='add_blog_post'),
    path('edit/<int:post_id>/', views.edit_blog_post, name='edit_blog_post'),
    path('', views.blog_list, name='blog_list'),
]
