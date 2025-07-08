from uuid import uuid4
from django.db import models
from cloudinary.models import CloudinaryField
from btre.settings import CLOUDINARY_FOLDER
# Create your models here.
class Realtor(models.Model):
  class Meta:
    verbose_name = 'Realtor'
    verbose_name_plural = f'{verbose_name}s'
    db_table = f'{verbose_name.lower()}s'
  id = models.UUIDField(
    primary_key = True,
    default = uuid4,
    editable = False
  )
  first_name = models.CharField()
  last_name = models.CharField()
  photo = CloudinaryField(
    'Photo',
    folder = CLOUDINARY_FOLDER
  )
  description = models.TextField(
    blank = True
  )
  email_address = models.EmailField()
  phone_number = models.CharField()
  is_mvp = models.BooleanField(
    default = False
  )
  created_at = models.DateTimeField(
    auto_now_add = True
  )
  updated_at = models.DateTimeField(
    auto_now = True
  )
  def __str__(self: 'Realtor') -> str:
    return f'{self.first_name} {self.last_name}'