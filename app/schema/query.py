from graphene import ObjectType, String, Boolean, List, Field, ID

from .types import Book, User
from app.data import books, users


class Query(ObjectType):
    hello = String()
    another = Boolean()
    all_books = List(Book)
    all_users = List(User)
    user = Field(lambda: User, id=ID(required=True))

    def resolve_hello(parent, info):
        return "Hello"

    def resolve_another(parent, info):
        return True

    def resolve_all_books(parent, info):
        return books

    def resolve_all_users(parent, info):
        return users

    def resolve_user(parent, info, **kwargs):
        user_id = kwargs.get('id', None)
        found_user = [user for user in users if str(user['id']) == user_id]

        return None if len(found_user) == 0 else found_user[0]
