from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from btre.settings import SEND_EMAILS
from .models import Contact
# Create your views here.
def contact(request: Request) -> HttpResponse:
  if request.method == 'POST':
    # check for existing inquiry
    if request.user.is_authenticated:
      LISTING_ID = request.POST['listing_id']
      USER_ID = request.user_id
      has_contacted = Contact.objects.all().filter(
        listing_id = LISTING_ID,
        user_id = USER_ID
      )
      if has_contacted:
        messages.error(
          request,
          'You have an existing inquiry regarding this listing. Our realtor will reply soon!'
        )
        return redirect('/listings/'+LISTING_ID)
      else:
        LISTING = request.POST['listing']
        Contact(
          listing = LISTING,
          listing_id = LISTING_ID,
          first = request.POST['first'],
          last = request.POST['last'],
          email = request.POST['email'],
          phone = request.POST['phone'],
          message = request.POST['message'],
          user_id = USER_ID
        ).save()
        # send email
        if SEND_EMAILS:
          send_mail(
            'Property Listing Inquiry',
            f'There has been an inquiry regarding {LISTING}.',
            '', [
              request.POST['realtor_email']
            ],
            fail_silently = False
          )
        messages.success(
          request,
          'Your inquiry has been sent to our realtor. They will reply soon!'
        )
        return redirect('/listings/'+LISTING_ID)