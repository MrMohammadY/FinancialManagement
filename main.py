import os
from create_files import create_folder_user, create_folder_product
from login import login
from Users import User
from Delete_Edit_User import DeleteUser, EditUser
from Delete_Edit_Product import DeleteProduct, EditProduct
from Show_Product_User import show_user, search_user, show_product, \
    search_product
from Data import Data


def run():
    cwd_usr = os.getcwd() + '\\user'
    try:
        with open(f'{cwd_usr}/user.json', 'r') as fr:
            if len(fr.read()) == 0:
                create_folder_user()
    except:
        create_folder_user()

    cwd_data = os.getcwd() + '\\data'
    try:
        with open(f'{cwd_data}/data.json', 'r') as fr:
            if len(fr.read()) == 0:
                create_folder_product()
    except:
        create_folder_product()


def log():
    username = input('please enter your username: ').strip()
    password = input('please enter your password: ').strip()
    result = login(username, password)
    if result is not None:
        return result[0], result[1], result[2]


def menu():
    print(f'1. Create User\n'
          f'2. Delete User\n'
          f'3. Edit User\n'
          f'4. Show User\n'
          f'5. Search User\n'
          f'6. Create Product\n'
          f'7. Delete Product\n'
          f'8. Edit Product\n'
          f'9. Show Product\n'
          f'10. Search Product'
          )
    try:
        choice = int(input('please choice a number(1-8): '))
    except ValueError:
        print('Enter a Number')
        return menu()
    if choice in range(1, 11):
        return choice
    else:
        return menu()


if __name__ == '__main__':
    run()
    login_user = log()
    choice = menu()
    
    if choice == 1:
        if login_user[2]:
            username = input('please enter your username: ').strip()
            password = input('please enter your password: ').strip()
            confirm_pass = input('please confirm your password: ').strip()
            user_type = int(input('please enter 0(guest) or 1(admin): '))
            new = User(username, password, confirm_pass, user_type)
            create_user = new.create_user(new.check_pass(),
                                          new.check_username())
            new.insert_to_file(create_user)

    if choice == 2:
        if login_user[2]:
            username = input('please enter your username for delete: ').strip()
            password = input('please enter your password for delete: ').strip()
            delete = DeleteUser(username, password)
            delete.delete()

    if choice == 3:
        if login_user[2]:
            username = input('please enter your username for edit: ').strip()
            password = input('please enter your password for edit: ').strip()
            new_username = input(
                'please enter your new username for edit: ').strip()
            new_password = input(
                'please enter your new password for edit: ').strip()
            confirm_pass = input('please confirm your password: ').strip()
            user_type = int(input('please enter 0(guest) or 1(admin):'))
            edit = EditUser(username, password, new_username,
                            new_password, confirm_pass, user_type)
            edit.edit()

    if choice == 4:
        show_user()

    if choice == 5:
        username = input('please enter your username for search: ').strip()
        search_user(username)

    if choice == 6:
        if login_user[2]:
            upc = int((input('please enter upc product: ')))
            name = input('please enter name product: ').strip()
            price = int(input('please enter price product: '))
            number = int(input('please enter number product: '))
            new = Data(upc, name, price, number)
            create_product = new.create_product(new.check_upc(),
                                                new.check_name())
            new.insert_to_file(create_product)

    if choice == 7:
        if login_user[2]:
            upc = int((input('please enter upc product to delete: ')))
            name = input('please enter name product to delete: ').strip()
            delete = DeleteProduct(upc, name)
            delete.delete()

    if choice == 8:
        if login_user[2]:
            upc = int((input('please enter upc product: ')))
            name = input('please enter name product: ').strip()
            new_upc = int((input('please enter upc product for edit: ')))
            new_name = input('please enter name product for edit: ').strip()
            new_price = int(input('please enter price product for edit: '))
            new_number = int(input('please enter number product for edit: '))
            edit = EditProduct(upc, name, new_upc,
                               new_name, new_price, new_number)
            edit.edit_pro()

    if choice == 9:
        show_product()

    if choice == 10:
        upc = int(input('please enter upc for search: '))
        search_product(upc)
