from graphene import ID, String, Interface, ObjectType, ID, Int, List, Enum, NonNull

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

    isbn = String(required=True)
    name = String(required=True)
    authors = List(lambda: NonNull(User))

    async def resolve_authors(parent, info):
        print(info.context)
        _authors = parent.get('authors')
        # authors = [user_loader.load(author) for author in _authors]
        # print(authors)
        authors = await info.user_loader.load_many(_authors)
        print(authors)

        return [{"id": '86165d53-784f-4a97-932a-767e004cd7f3', "gender": Gender.FEMALE, "name": "Pamela Reddington", "age": 24}]
