from graphene import ID, String, Interface, ObjectType, ID, Int, List, Enum

from .enums import Gender


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

    isbn = String()
    name = String()
    authors = List(User)
