from promise import Promise
from promise.dataloader import DataLoader

from app.data import users


def get_user(key):
    filtered_users = [user for user in users if str(user.get('id')) == str(key)]
    return None if len(filtered_users) == 0 else filtered_users[0]


class UserLoader(DataLoader):
    def batch_load_fn(self, keys):
        # Here we return a promise that will result on the
        # corresponding user for each key in keys
        return [get_user(user_id) for user_id in keys]

