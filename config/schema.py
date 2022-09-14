import typing
import strawberry


def get_books():
    return [Book(title="Tate", author="Top G.")]


@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)


schema = strawberry.Schema(query=Query)
