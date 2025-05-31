from uuid import uuid4
from django.db import models
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
  listing = models.CharField()
  listing_id = models.IntegerField()
  first = models.CharField()
  last = models.CharField()
  email = models.CharField()
  phone = models.CharField()
  message = models.TextField(
    blank = True
  )
  user_id = models.IntegerField(
    blank = True
  )
  created_at = models.DateTimeField(
    auto_now_add = True
  )
  updated_at = models.DateTimeField(
    auto_now = True
  )
  def __str__(self: object) -> str:
    return f'{self.first} {self.last}'