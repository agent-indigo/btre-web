from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
# Create your views here.
def contact(request):
  if request.method == 'POST':
    listing = request.POST['listing']
    listing_id = request.POST['listing_id']
    realtor_email = request.POST['realtor_email']
    # check for existing inquiry
    if request.user.is_authenticated:
      user_id = request.user_id
      has_contacted = Contact.objects.all().filter(
        listing_id = listing_id,
        user_id = user_id
      )
      if has_contacted:
        messages.error(
          request,
          'You have an existing inquiry regarding this listing. Our realtor will reply soon!'
        )
        return redirect('/listings/'+listing_id)
      else:
        Contact(
          listing = listing,
          listing_id = listing_id,
          first = request.POST['first'],
          last = request.POST['last'],
          email = request.POST['email'],
          phone = request.POST['phone'],
          message = request.POST['message'],
          user_id = user_id
        ).save()
      # send email
      if settings.SEND_EMAILS:
        send_mail(
          'Property Listing Inquiry',
          f'There has been an inquiry regarding {listing}.',
          '', [
            realtor_email
          ],
          fail_silently = False
        )
        messages.success(
          request,
          'Your inquiry has been sent to our realtor. They will reply soon!'
        )
        return redirect('/listings/'+listing_id)