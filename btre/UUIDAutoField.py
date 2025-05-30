"""
UUID Auto Field
Can be set as the DEFAULT_AUTO_FIELD
in settings.py to use v4 UUIDs as
primary keys
"""
from django.db.models import AutoField
from uuid import uuid4
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.models import Model
class UUIDAutoField(AutoField):
  def __init__(
    self: object,
    *args: tuple[
      str,
      ...
    ],
    **kwargs: dict[
      str,
      str
    ]
  ) -> None:
    kwargs['default'] = uuid4
    kwargs['editable'] = False
    super().__init__(
      *args,
      **kwargs
    )
  def db_type(
    self: object,
    connection: BaseDatabaseWrapper
  ) -> str:
    return 'uuid'
  def pre_save(
    self: object,
    model_instance: Model,
    add: bool
  ) -> str:
    value = getattr(
      model_instance,
      self.attname
    )
    if value is None:
      value = uuid4()
      setattr(
        model_instance,
        self.attname,
        value
      )
    return value