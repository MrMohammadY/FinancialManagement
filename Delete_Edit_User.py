import json


class EditUser:
    def __init__(self, username_find, password_find, new_username,
                 new_password, new_confirm_pass, new_type):
        self.username_find = username_find
        self.password_find = password_find
        self.new_username = new_username
        self.new_password = new_password
        self.new_confirm_pass = new_confirm_pass
        self.new_type = new_type

    def edit(self):
        if self.new_password == self.new_confirm_pass:
            with open('user/user.json', 'r') as fr:
                users = json.loads(fr.read())
                check_delete = False
                for index, u in enumerate(users['user']):

                    if (u['username'] == self.username_find) and \
                            (u['password'] == self.password_find):
                        users['user'].pop(index)
                        u['username'] = self.new_username
                        u['password'] = self.new_password
                        u['type'] = self.new_type
                        users['user'].append(u)
                        with open('user/user.json', 'w') as fw:
                            fw.write(json.dumps(users))
                            check_delete = True
        else:
            print('password is not correct')

        if check_delete:
            print(f'editing user : {self.username_find} to {self.new_username}')
        else:
            print(f'this username: {self.username_find} is not found')


class DeleteUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def delete(self):

        with open('user/user.json', 'r') as fr:
            users = json.loads(fr.read())
            if len(users['user']) == 1:
                print('you can\'t delete because has one user')
            else:
                check_delete = False
                for index, u in enumerate(users['user']):

                    if (u['username'] == self.username) and \
                            (u['password'] == self.password):
                        users['user'].pop(index)
                        with open('user/user.json', 'w') as fw:
                            fw.write(json.dumps(users))
                        check_delete = True

                if check_delete:
                    print(f'deleted user : {self.username}')
                else:
                    print(f'this username: {self.username} is not found')





