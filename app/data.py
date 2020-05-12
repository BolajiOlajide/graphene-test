from uuid import uuid4

from  app.schema.enums import Gender

users = [
    {"id": uuid4(), "gender": Gender.MALE, "name": "Carly Jones", "age": 18},
    {"id": uuid4(), "gender": Gender.FEMALE, "name": "Bianca James", "age": 28},
    {"id": uuid4(), "gender": Gender.MALE, "name": "Rick Grimes", "age": 16},
    {"id": uuid4(), "gender": Gender.FEMALE, "name": "Robyn Shank", "age": 15},
    {"id": uuid4(), "gender": Gender.MALE, "name": "Jonah Park", "age": 29},
    {"id": uuid4(), "gender": Gender.FEMALE, "name": "Lana Kane", "age": 20},
    {"id": uuid4(), "gender": Gender.MALE, "name": "Charles Dimali", "age": 30},
    {"id": uuid4(), "gender": Gender.FEMALE, "name": "Darlene Park", "age": 28},
    {"id": uuid4(), "gender": Gender.FEMALE, "name": "Pamela Reddington", "age": 24},
    {"id": uuid4(), "gender": Gender.FEMALE, "name": "Susan Stephenson", "age": 23},
]

books = [
    {"id": 1, "isbn": 139959342, "name": "48 laws of power", "authors": users[2:5]},
    {"id": 2, "isbn": 123530000, "name": "Subtle art of giving a F", "authors": [users[5]]},
    {"id": 3, "isbn": 405030002, "name": "Born a crime", "authors": users[0:2]},
    {"id": 4, "isbn": 200000004, "name": "Drawing for dummies", "authors": [users[1]]},
    {"id": 5, "isbn": 349590021, "name": "Understanding Nature", "authors": [users[3]]},
]
