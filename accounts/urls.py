from django.urls import path
from .views import dashboard, login, logout, register
urlpatterns = [
  path(
    'dashboard',
    dashboard,
    name = 'dashboard'
  ),
  path(
    'login',
    login,
    name = 'login'
  ),
  path(
    'logout',
    logout,
    name = 'logout'
  ),
  path(
    'register',
    register,
    name = 'register'
  )
]