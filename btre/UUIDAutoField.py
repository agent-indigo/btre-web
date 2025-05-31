"""
UUID Auto Field
Can be set as the DEFAULT_AUTO_FIELD
in settings.py to use v4 UUIDs as
primary keys
"""
from django.db.models import AutoField, UUIDField
from uuid import UUID, uuid4
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.models import Model
class UUIDAutoField(AutoField, UUIDField):
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
  ) -> UUID:
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
  def get_prep_value(
    self: object,
    value: UUID | None
  ) -> UUID | None:
    if value is None:
      return None
    if isinstance(
      value,
      UUID
    ):
      return value
    return UUID(value)
  def from_db_value(
    self: object,
    value: UUID | None,
    expression: object,
    connection: BaseDatabaseWrapper
  ) -> UUID | None:
    if value is None:
      return None
    if isinstance(
      value,
      UUID
    ):
      return value
    return UUID(value)