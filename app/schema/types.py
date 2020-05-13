from flask import g
from graphene import ID, String, Interface, ObjectType, ID, Int, List, Enum, NonNull

from .enums import Gender
from app.data import users


class BaseInterface(Interface):
    id = ID(required=True)


class User(ObjectType):
    class Meta:
        interfaces = (BaseInterface, )

    name = String()
    gender = Gender()
    age = Int()


class Book(ObjectType):
    class Meta:
        interfaces = (BaseInterface, )

    isbn = String(required=True)
    name = String(required=True)
    authors = List(lambda: NonNull(User))

    def resolve_authors(parent, info):
        _authors = parent.get('authors')
        return [user for user in users if user.get('id') in _authors]
