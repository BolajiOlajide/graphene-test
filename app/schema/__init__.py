from graphene import Schema

from .types import Book, User
from .query import Query
from .mutation import Mutation

schema = Schema(query=Query, types=[Book, User], mutation=Mutation)
