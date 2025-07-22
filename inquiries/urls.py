"""
Inquiries app views
"""
from django.urls import path
from .views import inquire
urlpatterns = [
    path(
        'inquire',
        inquire,
        name = 'inquire'
    )
]
