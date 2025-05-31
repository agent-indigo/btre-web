from django.contrib import admin
from .models import Inquiry
# Register your models here.
class InquiryAdmin(admin.ModelAdmin):
  list_display = (
    'first',
    'last',
    'email',
    'listing',
    'created_at'
  )
  list_display_links = (
    'first',
    'last',
    'email',
    'listing'
  )
  search_fields = (
    'first',
    'last',
    'email',
    'listing',
    'created_at'
  )
  list_per_page = 25
admin.site.register(
  Inquiry,
  InquiryAdmin
)