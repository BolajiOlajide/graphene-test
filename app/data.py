from uuid import uuid4

from  app.schema.enums import Gender

get_user_id = lambda x: x['id']

user_one_id = uuid4()
user_two_id = uuid4()
user_three_id = uuid4()
user_four_id = uuid4()
user_five_id = uuid4()
user_six_id = uuid4()

users = [
    {"id": user_one_id, "gender": Gender.MALE, "name": "Carly Jones", "age": 18},
    {"id": user_two_id, "gender": Gender.FEMALE, "name": "Bianca James", "age": 28},
    {"id": user_three_id, "gender": Gender.MALE, "name": "Rick Grimes", "age": 16},
    {"id": user_four_id, "gender": Gender.FEMALE, "name": "Robyn Shank", "age": 15},
    {"id": user_five_id, "gender": Gender.MALE, "name": "Jonah Park", "age": 29},
    {"id": user_six_id, "gender": Gender.FEMALE, "name": "Lana Kane", "age": 20},
    {"id": uuid4(), "gender": Gender.MALE, "name": "Charles Dimali", "age": 30},
    {"id": uuid4(), "gender": Gender.FEMALE, "name": "Darlene Park", "age": 28},
    {"id": uuid4(), "gender": Gender.FEMALE, "name": "Pamela Reddington", "age": 24},
    {"id": uuid4(), "gender": Gender.FEMALE, "name": "Susan Stephenson", "age": 23},
]

books = [
    {"id": 1, "isbn": 139959342, "name": "48 laws of power", "authors": [user_one_id, user_two_id]},
    {"id": 2, "isbn": 123530000, "name": "Subtle art of giving a F", "authors": [user_two_id]},
    {"id": 3, "isbn": 405030002, "name": "Born a crime", "authors": [user_three_id]},
    {"id": 4, "isbn": 200000004, "name": "Drawing for dummies", "authors": [user_four_id, user_five_id, user_six_id]},
    {"id": 5, "isbn": 349590021, "name": "Understanding Nature", "authors": [user_five_id]},
]
