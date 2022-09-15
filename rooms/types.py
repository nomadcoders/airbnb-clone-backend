import strawberry
from strawberry import auto
from . import models
from users.types import UserType


@strawberry.django.type(models.Room)
class RoomType:
    id: auto
    name: auto
    kind: auto
    owner: "UserType"
