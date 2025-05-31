from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import SafeText
from .models import Inquiry
# Register your models here.
class InquiryAdmin(admin.ModelAdmin):
  list_display = (
    'message',
    'listing_title',
    'first_name',
    'last_name',
    'email_address',
    'phone_number',
    'created_at'
  )
  list_display_links = (
    'message',
  )
  search_fields = (
    'message',
    'listing_title',
    'first_name',
    'last_name',
    'email_address',
    'phone_number',
    'created_at'
  )
  list_per_page = 25
  def first_name(
    self: object,
    inquiry: Inquiry
  ) -> SafeText | str:
    return format_html(
      '<a href="{url}">{name}</a>',
      url = reverse(
        'admin:auth_user_change',
        args = [
          inquiry.user_id.id
        ]
      ),
      name = inquiry.first_name
    ) if inquiry.user_id is not None else inquiry.first_name
  def last_name(
    self: object,
    inquiry: Inquiry
  ) -> SafeText | str:
    return format_html(
      '<a href="{url}">{name}</a>',
      url = reverse(
        'admin:auth_user_change',
        args = [
          inquiry.user_id.id
        ]
      ),
      name = inquiry.last_name
    ) if inquiry.user_id is not None else inquiry.last_name
  def email_address(
    self: object,
    inquiry: Inquiry
  ) -> SafeText:
    return format_html(
      '<a href="mailto:{email}">{email}</a>',
      email = inquiry.email_address
    )
  def phone_number(
    self: object,
    inquiry: Inquiry
  ) -> SafeText:
    return format_html(
      '<a href="tel:{phone}">{phone}</a>',
      phone = inquiry.phone_number
    )
admin.site.register(
  Inquiry,
  InquiryAdmin
)