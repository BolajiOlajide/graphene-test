from uuid import uuid4

from graphene import Mutation, String, Boolean, Field, ObjectType, Int

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


class Mutation(ObjectType):
    create_user = CreateUser.Field()
