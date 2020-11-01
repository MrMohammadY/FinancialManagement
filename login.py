import json
import os


def login(username, password):
    check = False
    cwd_user = os.getcwd() + '\\user'
    with open(f'{cwd_user}/user.json', 'r') as fr:
        users = json.loads(fr.read())
        for u in users['user']:
            if u['username'] == username and u['password'] == password:
                user_name = u['username']
                user_pass = u['password']
                user_type = u['type']
                check = True
    if check:
        return user_name, user_pass, user_type
    else:
        print('This user name not exist!')