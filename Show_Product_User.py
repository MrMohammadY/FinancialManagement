import json


def show_product():
    with open('data/data.json', 'r') as fr:
        data = json.loads(fr.read())
        for pro in data['product']:
            print(f'upc: {pro["upc"]} name product: {pro["name"]}'
                  f' price: {pro["price"]} number: {pro["number"]}')


def search_product(upc):
    with open('data/data.json', 'r') as fr:
        data = json.loads(fr.read())
        for pro in data['product']:
            if upc == pro['upc']:
                print(f'upc: {pro["upc"]} name product: {pro["name"]}'
                      f' price: {pro["price"]} number: {pro["number"]}')


def show_user():
    with open('user/user.json', 'r') as fr:
        data = json.loads(fr.read())
        for user in data['user']:
            print(f'Username: {user["username"]}'
                  f' Type: {"Admin" if user["type"] == 1 else "Guest"}')


def search_user(username):
    with open('user/user.json', 'r') as fr:
        data = json.loads(fr.read())
        for user in data['user']:
            if username == user['username']:
                print(f'Username: {user["username"]}'
                      f' Type: {"Admin" if user["type"] == 1 else "Guest"}')
