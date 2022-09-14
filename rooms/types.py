import strawberry
import typing
from strawberry import auto
from reviews.types import Review
from . import models


def resolve_reviews(self, page: int) -> typing.List[Review]:
    print(self)
    return []


@strawberry.django.type(models.Room)
class Room:
    id: auto
    name: auto
    emoji: str
    reviews: typing.List["Review"] = strawberry.field(resolver=resolve_reviews)

    @strawberry.field
    def emoji(self, info) -> str:
        print(self.name)
        return self.name
