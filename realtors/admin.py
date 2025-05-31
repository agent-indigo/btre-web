from django.contrib import admin
from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
  list_display = (
    'first',
    'last',
    'email',
    'created_at',
    'updated_at'
  )
  list_display_links = (
    'first',
    'last',
    'email'
  )
  search_fields = (
    'first',
    'last',
    'email',
    'created_at',
    'updated_at'
  )
  list_per_page = 25
admin.site.register(
  Realtor,
  RealtorAdmin
)