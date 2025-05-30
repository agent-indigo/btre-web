from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField
from btre.settings import CLOUDINARY_FOLDER
# Create your models here.
class Realtor(models.Model):
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
  hire_date = models.DateTimeField(
    default = datetime.now,
    blank = True
  )
  def __str__(self: object) -> str:
    return f'{self.first} {self.last}'