from django.contrib.messages.api import success
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import Post

class PostListView(ListView):
    
    model = Post
    
    # The default template is 'blog/post_list.html'
    template_name = 'blog/home.html'
    
    # Otherwise the object name is `object`
    context_object_name = 'posts'
    
    # Order from newest to oldest
    ordering = ['-date_posted']
    
    paginate_by = 5


class UserPostListView(ListView):
    
    model = Post
    
    template_name = 'blog/user_posts.html'
    
    context_object_name = 'posts'
    
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
class PostDetailView(DetailView):
    
    model = Post
    
    context_object_name = 'post'


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    model = Post
    
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Put the mixin as the first!!!
class PostCreateView(LoginRequiredMixin, CreateView):
    
    model = Post
    
    # Need to tell what do you what in the form
    fields = ['title', 'content']

    def form_valid(self, form):
        '''Set the author of the post to be the current user'''
        form.instance.author = self.request.user
        return super().form_valid(form)


# Make sure a user can only update his own posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Post
    
    # Need to tell what do you what in the form
    fields = ['title', 'content']

    def form_valid(self, form):
        '''Set the author of the post to be the current user'''
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        # The post we are trying to update
        post = self.get_object()
        return self.request.user == post.author
        
def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html')
