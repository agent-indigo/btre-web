from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import SafeText
from .models import Listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
  list_display = (
    'title',
    'address',
    'city',
    'state',
    'zipcode',
    'bedrooms',
    'bathrooms',
    'garage',
    'sqft',
    'lot_size',
    'price',
    'is_published',
    'realtor_first_name',
    'realtor_last_name',
    'created_at',
    'updated_at'
  )
  list_display_links = (
    'title',
  )
  list_filter = (
    'city',
    'state',
    'zipcode',
    'bedrooms',
    'bathrooms',
    'garage',
    'sqft',
    'lot_size',
    'price',
    'realtor_id__first_name',
    'realtor_id__last_name',
    'is_published',
    'created_at'
  )
  list_editable = (
    'is_published',
  )
  search_fields = (
    'title',
    'address',
    'city',
    'state',
    'zipcode',
    'description',
    'price',
    'bedrooms',
    'bathrooms',
    'garage',
    'sqft',
    'lot_size',
    'realtor_id__first_name',
    'realtor_id__last_name',
    'created_at'
  )
  list_per_page = 25
  def realtor_first_name(
    self: object,
    listing: Listing
  ) -> SafeText:
    return format_html(
      '<a href="{url}">{name}</a>',
      url = reverse(
        'admin:realtors_realtor_change',
        args = [
          listing.realtor_id.id
        ]
      ),
      name = listing.realtor_id.first_name
    )
  def realtor_last_name(
    self: object,
    listing: Listing
  ) -> SafeText:
    return format_html(
      '<a href="{url}">{name}</a>',
      url = reverse(
        'admin:realtors_realtor_change',
        args = [
          listing.realtor_id.id
        ]
      ),
      name = listing.realtor_id.last_name
    )
admin.site.register(
  Listing,
  ListingAdmin
)