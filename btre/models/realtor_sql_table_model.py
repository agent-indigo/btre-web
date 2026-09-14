"""
Realtor SQL table model
"""
from django.db import models
from cloudinary.models import CloudinaryField
from .sql_model_base import SqlModelBase
from ..settings import CLOUDINARY_FOLDER
class Realtor(SqlModelBase):
    """
    Realtor SQL table model
    """
    class Meta:
        """
        Realtor SQL table model meta class
        """
        verbose_name = 'Realtor'
        verbose_name_plural = f'{verbose_name}s'
        db_table = verbose_name_plural.lower()
    first_name = models.CharField()
    last_name = models.CharField()
    photo = CloudinaryField(
        'Photo',
        folder = CLOUDINARY_FOLDER
    )
    description = models.TextField()
    email_address = models.EmailField()
    phone_number = models.CharField()
    is_mvp = models.BooleanField(
        default = False
    )
