from django.contrib import admin
from .models import Listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
  list_display = (
    'title',
    'price',
    'is_published',
    'realtor_id',
    'created_at',
    'updated_at'
  )
  list_display_links = (
    'title',
  )
  list_filter = (
    'realtor_id',
  )
  list_editable = (
    'is_published',
  )
  search_fields = (
    'title',
    'description',
    'address',
    'city',
    'state',
    'zipcode',
    'price',
    'created_at',
    'updated_at'
  )
  list_per_page = 25
admin.site.register(
  Listing,
  ListingAdmin
)