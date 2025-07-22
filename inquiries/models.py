"""
Inquiries app SQL table models
"""
from uuid import uuid4
from django.db import models
# Create your models here.
class Inquiry(models.Model):
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
        to = 'auth.User',
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
