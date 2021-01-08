from django.urls import path

from . import views
from .views import (
    PostDetailView, 
    PostListView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    UserPostListView
)

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # The `PostDetailView` expects a variable called `pk` by default
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # The `PostCreateView` expects a template called `post_form.html` by default
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    # The `PostDeleteView` will ask for confirmation
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]
