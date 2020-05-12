from graphene import Schema

from .types import Book, User
from .query import Query

schema = Schema(query=Query, types=[Book, User])
