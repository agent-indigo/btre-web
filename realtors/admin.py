from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import SafeText
from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
  list_display = (
    'first_name',
    'last_name',
    'email',
    'phone',
    'is_mvp',
    'created_at',
    'updated_at'
  )
  list_display_links = (
    'first_name',
    'last_name'
  )
  search_fields = (
    'first_name',
    'last_name',
    'email_address',
    'phone_number',
    'created_at',
    'updated_at'
  )
  list_per_page = 25
  def email(
    self: object,
    realtor: Realtor
  ) -> SafeText:
    return format_html(
      '<a href="mailto:{email}">{email}</a>',
      email = realtor.email_address
    )
  email.short_description = 'Email Address'
  def phone(
    self: object,
    realtor: Realtor
  ) -> SafeText:
    return format_html(
      '<a href="tel:{phone}">{phone}</a>',
      phone = realtor.phone_number
    )
  phone.short_description = 'Phone Number'
admin.site.register(
  Realtor,
  RealtorAdmin
)