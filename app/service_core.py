from abc import ABC

from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.models import QuerySet, Model


class BaseService(ABC):
    __slots__ = ("queryset",)

    _queryset: QuerySet

    @classmethod
    def get_one(cls, object_id) -> Model:
        if not object_id:
            raise ValidationError("id can't be empty")

        try:
            product = cls._queryset.get(id=object_id)
            return product
        except ObjectDoesNotExist:
            raise ValidationError("object not found")

    @classmethod
    def get_by_params(cls, **kwargs):
        return cls._queryset.filter(**kwargs)
