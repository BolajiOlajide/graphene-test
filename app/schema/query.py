from graphene import ObjectType, String, Boolean, List

from .types import Book, User
from app.data import books, users


class Query(ObjectType):
    hello = String()
    another = Boolean()
    all_books = List(Book)
    all_users = List(User)

    def resolve_hello(self, info):
        return "Hello"

    def resolve_another(self, info):
        return True

    def resolve_all_books(self, info):
        return books

    def resolve_all_users(self, info):
        return users
