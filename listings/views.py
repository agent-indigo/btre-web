from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'page_title': 'Listings'
    }
    return render(request, 'listings/listings.html', context)

def listing(request):
    context = {
        'page_title': 'Listing'
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    context = {
        'page_title': 'Search'
    }
    return render(request, 'listings/search.html', context)
