import json


class User:

    def __init__(self, username, password, confirm_password, user_type=0):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password
        self.user_type = user_type

    def check_pass(self):
        if self.password == self.confirm_password:
            return True
        else:
            return False

    def check_username(self):
        check = True

        with open('user/user.json', 'r') as fr:
            data = json.loads(fr.read())

            for u in data['user']:
                if u['username'] == self.username:
                    check = False

        return check

    def create_user(self, check_pass, check_user):

        if check_user is False:
            print('Your UserName is exist please choice another UserName!')

        elif check_pass is False:
            print('Your password is not correct!')

        elif (check_pass and check_user) is False:
            print('Your UserName is exist please choice another UserName!\n'
                  'Your password is not correct!')

        else:
            new_user = {
                'username': self.username,
                'password': self.password,
                'type': self.user_type
            }
            return new_user

    def insert_to_file(self, new_user):

        with open('user/user.json', 'r') as fr:
            data = json.loads(fr.read())
            data['user'].append(new_user)

            with open('user/user.json', 'w') as fw:
                fw.write(json.dumps(data))
                print('User Created Your Username created: ', self.username)
