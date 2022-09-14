import strawberry
from strawberry import auto
from . import models


@strawberry.django.type(models.Review)
class Review:
    id: auto
    payload: auto
