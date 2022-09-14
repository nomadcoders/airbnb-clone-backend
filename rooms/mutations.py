import strawberry
from strawberry.types import Info


@strawberry.mutation
def add_book(
    self,
    info: Info,
    title: str,
    author: str,
) -> str:
    print(info.context.request.user)
    return f"{title} {author}"
