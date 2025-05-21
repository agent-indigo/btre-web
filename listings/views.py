from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.urls import reverse
from .options import beds, prices, states
from .models import Listing
# Create your views here.
def index(request):
  return render(
    request,
    'listings/listings.html', {
      'breadcrumb': [{
        'label': 'Listings',
        'url': None
      }],
      'listings': Paginator(
        Listing.objects.order_by('-list_date').filter(
          is_published = True
        ),
        6
      ).get_page(request.GET.get('page'))
    }
  )
def listing(
  request,
  listing_id
):
  listing = get_object_or_404(
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
        'label': listing.title,
        'url': None
      }],
      'listing': listing
    }
  )
def search(request):
  queryset_list = Listing.objects.order_by('-list_date')
  # keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(
        description__icontains = keywords
      )
  # city
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(
        city__iexact = city
      )
  # state
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(
        state__iexact = state
      )
  # bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(
        bedrooms__iexact = bedrooms
      )
  # price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(
        price__lte = price
      )
  return render(
    request,
    'listings/search.html', {
      'breadcrumb': [{
        'label': 'Listings',
        'url': reverse('listings'
      )}, {
        'label': 'Search',
        'url': None
      }],
      'beds': beds,
      'listings': queryset_list,
      'prices': prices,
      'states': states,
      'values': request.GET
    }
  )