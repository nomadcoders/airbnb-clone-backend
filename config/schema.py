import typing
import strawberry


@strawberry.type
class Book:
    title: str
    author: str


books = [Book(title="Tate", author="Top G.")]


def get_books():
    return books


@strawberry.type
class Query:
    # books: typing.List[Book] = strawberry.field(resolver=get_books)
    @strawberry.field
    def books(self) -> typing.List[Book]:
        return books


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        new_book = Book(title=title, author=author)
        books.append(new_book)
        return new_book


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
