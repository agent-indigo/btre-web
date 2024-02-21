from django.shortcuts import render

from listings.options import beds, prices, states
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'beds': beds,
        'listings': listings,
        'prices': prices,
        'states': states
    }

    return render(request, 'pages/index.html', context)

def about(request):
    breadcrumb = [
        {'label': 'About', 'url': None}
    ]

    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # get mvp
    mvps = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'breadcrumb': breadcrumb,
        'mvps': mvps,
        'realtors': realtors
    }

    return render(request, 'pages/about.html', context)
