import typing
from strawberry.types import Info
from django.contrib.auth import login
from users.models import User
from . import models
from . import types


def resolve_rooms() -> typing.List[types.Room]:
    return models.Room.objects.all()


def resolve_login(info: Info) -> bool:
    user = User.objects.get(pk=1)
    login(info.context.request, user)
    return True
