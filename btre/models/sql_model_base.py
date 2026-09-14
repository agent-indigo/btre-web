"""
Abstract class providing primary key and timestamps
for all database tables not provided by Django
"""
from uuid import uuid4
from django.db import models
class SqlModelBase(models.Model):
    """
    Abstract class providing primary key and timestamps
    for all database tables not provided by Django
    """
    class Meta:
        """
        Model base meta class
        """
        abstract = True
    id = models.UUIDField(
        primary_key = True,
        default = uuid4,
        editable = False
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )
