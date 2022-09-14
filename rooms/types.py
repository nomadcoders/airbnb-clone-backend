import strawberry
from strawberry import auto
from . import models


@strawberry.django.type(models.Room)
class Room:
    id: auto
    name: auto
    emoji: str

    @strawberry.field
    def emoji(self, info) -> str:
        print(self.name)
        return self.name
