"""
Listings app views
"""
from urllib.request import Request
from uuid import UUID
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.urls import reverse
from .options import BEDS, PRICES, STATES
from .models import Listing
# Create your views here.
def index(request: Request) -> HttpResponse:
    """
    Listings page view
    """
    return render(
        request,
        'listings/listings.html', {
            'breadcrumb': [{
                'label': 'Listings',
                'url': None
            }],
            'listings': Paginator(
                Listing.objects.order_by('-created_at').filter(
                    is_published = True
                ),
                6
            ).get_page(request.GET.get('page'))
        }
    )
def listing(
    request: Request,
    listing_id: UUID
) -> HttpResponse:
    """
    Listing page view
    """
    LISTING = get_object_or_404(
        Listing,
        pk = listing_id
    )
    return render(
        request,
        'listings/listing.html', {
            'breadcrumb': [{
                'label': 'Listings',
                'url': reverse('listings')
            }, {
                'label': LISTING.title,
                'url': None
            }],
            'listing': LISTING
        }
    )
def search(request: Request) -> HttpResponse:
    """
    Search view
    """
    listings = Listing.objects.order_by('-created_at')
    # keywords
    if 'keywords' in request.GET:
        KEYWORDS = request.GET['keywords']
        if KEYWORDS:
            listings = listings.filter(
                description__icontains = KEYWORDS
            )
    # city
    if 'city' in request.GET:
        CITY = request.GET['city']
        if CITY:
            listings = listings.filter(
                city__iexact = CITY
            )
    # state
    if 'state' in request.GET:
        STATE = request.GET['state']
        if STATE:
            listings = listings.filter(
                state__iexact = STATE
            )
    # bedrooms
    if 'bedrooms' in request.GET:
        BEDROOMS = request.GET['bedrooms']
        if BEDROOMS:
            listings = listings.filter(
                bedrooms__iexact = BEDROOMS
            )
    # price
    if 'price' in request.GET:
        PRICE = request.GET['price']
        if PRICE:
            listings = listings.filter(
                price__lte = PRICE
            )
    return render(
        request,
        'listings/search.html', {
            'breadcrumb': [{
                'label': 'Listings',
                'url': reverse('listings')
            }, {
                'label': 'Search',
                'url': None
            }],
            'beds': BEDS,
            'listings': listings,
            'prices': PRICES,
            'states': STATES,
            'values': request.GET
        }
    )
