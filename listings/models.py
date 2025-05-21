from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField
from btre.settings import CLOUDINARY_FOLDER
from realtors.models import Realtor
# Create your models here.
class Listing(models.Model):
  realtor = models.ForeignKey(
    Realtor,
    on_delete = models.DO_NOTHING
  )
  title = models.CharField()
  address = models.CharField()
  city = models.CharField()
  state = models.CharField()
  zipcode = models.CharField(
    max_length = 5
  )
  description = models.TextField(
    blank = True
  )
  price = models.DecimalField(
    max_digits = 12,
    decimal_places = 2
  )
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(
    max_digits = 2,
    decimal_places = 1
  )
  garage = models.IntegerField(
    default = 0
  )
  sqft = models.DecimalField(
    max_digits = 6,
    decimal_places = 1
  )
  lot_size = models.DecimalField(
    max_digits = 5,
    decimal_places = 1
  )
  photo_main = CloudinaryField(
    'image',
    folder = CLOUDINARY_FOLDER
  )
  photo_1 = CloudinaryField(
    'image',
    folder = CLOUDINARY_FOLDER,
    blank = True
  )
  photo_2 = CloudinaryField(
    'image',
    folder = CLOUDINARY_FOLDER,
    blank = True
  )
  photo_3 = CloudinaryField(
    'image',
    folder = CLOUDINARY_FOLDER,
    blank = True
  )
  photo_4 = CloudinaryField(
    'image',
    folder = CLOUDINARY_FOLDER,
    blank = True
  )
  photo_5 = CloudinaryField(
    'image',
    folder = CLOUDINARY_FOLDER,
    blank = True
  )
  photo_6 = CloudinaryField(
    'image',
    folder = CLOUDINARY_FOLDER,
    blank = True
  )
  is_published = models.BooleanField(
    default = True
  )
  list_date = models.DateTimeField(
    default = datetime.now,
    blank = True
  )
  def __str__(self):
    return self.title