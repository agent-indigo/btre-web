"""
Inquiry SQL table model
"""
from django.db import models
from .sql_model_base import SqlModelBase
class Inquiry(SqlModelBase):
    """
    Inquiry SQL table model
    """
    class Meta:
        """
        Inquiry SQL table model meta class
        """
        verbose_name = 'Inquiry'
        verbose_name_plural = 'Inquiries'
        db_table = verbose_name_plural.lower()
    listing = models.ForeignKey(
        to = 'Listing',
        on_delete = models.CASCADE
    )
    first_name = models.CharField()
    last_name = models.CharField()
    email_address = models.EmailField()
    phone_number = models.CharField()
    message = models.TextField()
    user = models.ForeignKey(
        to = 'auth.User',
        on_delete = models.CASCADE,
        blank = True
    )
