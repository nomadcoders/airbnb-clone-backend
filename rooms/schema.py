import typing
import strawberry
from . import types
from . import queries
from . import mutations
from strawberry.permission import BasePermission
from strawberry.types import Info


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    # This method can also be async!
    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        return False


@strawberry.type
class Query:
    rooms: typing.List[types.Room] = strawberry.field(
        resolver=queries.resolve_rooms,
        permission_classes=[IsAuthenticated],
    )
    login: bool = strawberry.field(resolver=queries.resolve_login)


@strawberry.type
class Mutation:
    add_book = mutations.add_book
