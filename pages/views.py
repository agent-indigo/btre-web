"""
Pages app views
"""
from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render
from listings.options import BEDS, PRICES, STATES
from listings.models import Listing
from realtors.models import Realtor
# Create your views here.
def index(request: Request) -> HttpResponse:
    """
    Home page view
    """
    return render(
        request,
        'pages/index.html', {
            'beds': BEDS,
            'listings': Listing.objects.order_by('-created_at').filter(
                is_published = True
            )[:3],
            'prices': PRICES,
            'states': STATES
        }
    )
def about(request: Request) -> HttpResponse:
    """
    About page view
    """
    return render(
        request,
        'pages/about.html', {
            'breadcrumb': [{
                'label': 'About',
                'url': None
            }],
            'mvps': Realtor.objects.all().filter(
                is_mvp = True
            ),
            'realtors': Realtor.objects.order_by('-created_at')
        }
    )
