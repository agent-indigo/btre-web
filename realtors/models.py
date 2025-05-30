from django.db import models
from cloudinary.models import CloudinaryField
from btre.settings import CLOUDINARY_FOLDER
# Create your models here.
class Realtor(models.Model):
  class Meta:
    verbose_name = 'Realtor'
    verbose_name_plural = f'{verbose_name}s'
    db_table = f'{verbose_name.lower()}s'
  first = models.CharField()
  last = models.CharField()
  photo = CloudinaryField(
    'image',
    folder = CLOUDINARY_FOLDER
  )
  description = models.TextField(
    blank = True
  )
  phone = models.CharField()
  email = models.CharField()
  is_mvp = models.BooleanField(
    default = False
  )
  created_at = models.DateTimeField(
    auto_now_add = True
  )
  updated_at = models.DateTimeField(
    auto_now = True
  )
  def __str__(self: object) -> str:
    return f'{self.first} {self.last}'