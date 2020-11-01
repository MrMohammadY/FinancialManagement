import os
import json


def create_folder_user():
    try:
        cwd_user = os.getcwd() + '\\user\\'

        os.mkdir(cwd_user)
        print('You should create first User!')
        username = input('please Enter Your Username: ')
        password = input('please Enter Your Password: ')
        confirm_pass = input('please Confirm your password: ')
        type_user = 1
        if password != confirm_pass:
            return create_folder_user()

        data = {'user':
            [
                {'username': username, 'password': password, 'type': type_user}
            ]
        }
        with open(f'{cwd_user}/user.json', 'w') as fw:
            fw.write(json.dumps(data))
    except OSError as error:
        pass


def create_folder_product():
    try:
        cwd_data = os.getcwd() + '\\data\\'
        os.mkdir(cwd_data)
        print('You should create first product!')
        try:
            upc = int(input('please enter your upc product: '))
            name = input('please enter your name product: ')
            price = int(input('please enter your price product: '))
            number = int(input('please enter your number of product: '))
        except ValueError:
            print(
                'please check the value name should string and other should int'
            )
            return create_folder_product()
        data = {'product': [{'upc': upc, 'name': name,
                             'price': price, 'number': number}]}
        with open(f'{cwd_data}/data.json', 'w') as fw:
            fw.write(json.dumps(data))
    except OSError as error:
        pass

