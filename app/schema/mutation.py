from uuid import uuid4

from graphene import Mutation, String, Boolean, Field, ObjectType, Int, List, ID, NonNull

from .types import Book, User
from app.data import books, users
from .enums import Gender


class CreateUser(Mutation):
    class Arguments:
        name = String(required=True)
        gender = String(required=True)
        age = Int(required=True)

    ok = Boolean()
    user = Field(lambda: User)

    def mutate(root, info, **kwargs):
        gender = Gender.get(kwargs.pop('gender'))
        new_user = dict(**kwargs, id=uuid4(), gender=gender)
        users.append(new_user)
        ok = True
        return CreateUser(user=new_user, ok=ok)


class CreateBook(Mutation):
    class Arguments:
        isbn = String(required=True)
        name = String(required=True)
        authors = List(NonNull(ID))

    ok = Boolean()
    book = Field(lambda: Book)

    def mutate(root, info, **kwargs):
        new_book_id = books[-1]['id'] + 1
        new_book = dict(**kwargs, id=new_book_id, authors=[])
        books.push(new_book)


class Mutation(ObjectType):
    create_user = CreateUser.Field()
    create_book = CreateBook.Field()
