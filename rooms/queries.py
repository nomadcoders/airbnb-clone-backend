import typing
from . import models
from . import types


def resolve_rooms() -> typing.List[types.Room]:
    return models.Room.objects.all()
