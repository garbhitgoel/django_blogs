from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {   
        'author': 'Garbhit Goel',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 01, 2026'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 02, 2026'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
