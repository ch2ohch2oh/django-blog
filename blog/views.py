from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

posts = [
    {
        'author': 'Einstein',
        'title': 'E=mc2',
        'content': 'Top secret',
        'date_posted': 'August 12, 2020'
    },
    {
        'author': 'Newton',
        'title': 'F=ma',
        'content': 'Second law',
        'date_posted': 'August 12, 2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html')
