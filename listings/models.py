from uuid import uuid4
from django.db import models
from cloudinary.models import CloudinaryField
from btre.settings import CLOUDINARY_FOLDER
from realtors.models import Realtor
# Create your models here.
class Listing(models.Model):
  class Meta:
    verbose_name = 'Listing'
    verbose_name_plural = f'{verbose_name}s'
    db_table = f'{verbose_name.lower()}s'
  id = models.UUIDField(
    primary_key = True,
    default = uuid4,
    editable = False
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
  exterior = CloudinaryField(
    'Exterior',
    folder = CLOUDINARY_FOLDER
  )
  interior_1 = CloudinaryField(
    'Interior 1',
    folder = CLOUDINARY_FOLDER,
  )
  interior_2 = CloudinaryField(
    'Interior 2',
    folder = CLOUDINARY_FOLDER,
  )
  interior_3 = CloudinaryField(
    'Interior 3',
    folder = CLOUDINARY_FOLDER,
  )
  interior_4 = CloudinaryField(
    'Interior 4',
    folder = CLOUDINARY_FOLDER,
  )
  interior_5 = CloudinaryField(
    'Interior 5',
    folder = CLOUDINARY_FOLDER,
    blank = True
  )
  interior_6 = CloudinaryField(
    'Interior 6',
    folder = CLOUDINARY_FOLDER,
    blank = True
  )
  is_published = models.BooleanField(
    default = True
  )
  realtor_id = models.ForeignKey(
    Realtor,
    on_delete = models.DO_NOTHING
  )
  created_at = models.DateTimeField(
    auto_now_add = True
  )
  updated_at = models.DateTimeField(
    auto_now = True
  )
  def __str__(self: object) -> str:
    return self.title