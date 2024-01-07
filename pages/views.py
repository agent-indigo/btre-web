from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    context = {
        'page_title': 'About'
    }
    return render(request, 'pages/about.html', context)
