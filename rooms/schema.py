import typing
import strawberry
from . import types
from . import queries


@strawberry.type
class Query:
    rooms: typing.List[types.Room] = strawberry.field(resolver=queries.resolve_rooms)
