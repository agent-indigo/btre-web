from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
  listing = models.CharField()
  listing_id = models.IntegerField()
  first = models.CharField()
  last = models.CharField()
  email = models.CharField()
  phone = models.CharField()
  message = models.TextField(
    blank = True
  )
  contact_date = models.DateTimeField(
    default = datetime.now,
    blank = True
  )
  user_id = models.IntegerField(
    blank = True
  )
  def __str__(self):
    return f'{self.first} {self.last}'