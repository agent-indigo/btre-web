from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Inquiry(models.Model):
  class Meta:
    verbose_name = 'Inquiry'
    verbose_name_plural = 'Inquiries'
    db_table = 'inquiries'
  id = models.UUIDField(
    primary_key = True,
    default = uuid4,
    editable = False
  )
  listing_title = models.CharField()
  listing_id = models.IntegerField()
  first_name = models.CharField()
  last_name = models.CharField()
  email_address = models.EmailField()
  phone_number = models.CharField()
  message = models.TextField(
    blank = True
  )
  user_id = models.ForeignKey(
    User,
    on_delete = models.DO_NOTHING,
    blank = True
  )
  created_at = models.DateTimeField(
    auto_now_add = True
  )
  updated_at = models.DateTimeField(
    auto_now = True
  )
  def __str__(self: 'Inquiry') -> str:
    return f'{self.message} {self.listing_title} {self.created_at}'