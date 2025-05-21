from django.shortcuts import render
from listings.options import beds, prices, states
from listings.models import Listing
from realtors.models import Realtor
# Create your views here.
def index(request):
  return render(
    request,
    'pages/index.html', {
      'beds': beds,
      'listings': Listing.objects.order_by('-list_date').filter(
        is_published = True
      )[:3],
      'prices': prices,
      'states': states
    }
  )
def about(request):
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
      'realtors': Realtor.objects.order_by('-hire_date')
    }
  )