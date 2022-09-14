import typing
import strawberry
from . import types
from . import queries
from . import mutations


@strawberry.type
class Query:
    rooms: typing.List[types.Room] = strawberry.field(resolver=queries.resolve_rooms)


@strawberry.type
class Mutation:
    add_book = mutations.add_book
