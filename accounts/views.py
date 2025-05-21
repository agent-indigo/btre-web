from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.urls import reverse
from contacts.models import Contact
# Create your views here.
def dashboard(request):
  return render(
    request,
    'accounts/dashboard.html', {
      'breadcrumb': [{
        'label': 'Dashboard',
        'url': None
      }],
      'contacts': Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)
    }
  )
def login(request):
  if request.method == 'POST':
    user = auth.authenticate(
      username = request.POST['username'],
      password = request.POST['password']
    )
    if user is not None:
      auth.login(
        request,
        user
      )
      if user.is_staff:
        return redirect(reverse('admin:index'))
      else:
        messages.success(
          request,
          'You are now logged in.'
        )
        return redirect('dashboard')
    else:
      messages.error(
        request,
        'Invalid credentials.'
      )
      return redirect('login')
  else:
    return render(
      request,
      'accounts/login.html'
    )
def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(
      request,
      'You are now logged out.'
    )
    return redirect('index')
def register(request):
  if request.method == 'POST':
    # get form values
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    # check if passwords match
    if password == password2:
      # check username
      if User.objects.filter(username = username).exists():
        messages.error(
          request,
          'That username is taken.'
        )
        return redirect('register')
      else:
        # check email
        if User.objects.filter(email = email).exists():
          messages.error(
            request,
            'An account with that email address already exists.'
          )
          return redirect('register')
        else:
          # create user and immediately log in
          auth.login(
            request,
            User.objects.create_user(
              username = username,
              password = password,
              email = email,
              first_name = request.POST['first_name'],
              last_name = request.POST['last_name']
            )
          )
          messages.success(
            request,
            'You are now logged in.'
          )
          return redirect('dashboard')
    else:
      messages.error(
        request,
        'Passwords do not match'
      )
      return redirect('register')
  else:
    return render(
      request,
      'accounts/register.html'
    )