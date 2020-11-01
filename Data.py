import json


class Data:

    def __init__(self, upc, name, price, number=1):
        self.upc = upc
        self.name = name
        self.price = price
        self.number = number

    def check_upc(self):
        check = True
        with open('data/data.json', 'r') as fr:
            data = json.loads(fr.read())
            for d in data['product']:
                if d['upc'] == self.upc:
                    check = False
        return check

    def check_name(self):
        check = True
        with open('data/data.json', 'r') as fr:
            data = json.loads(fr.read())
            for d in data['product']:
                if d['name'] == self.name:
                    check = False
        return check

    def create_product(self, check_upc, check_name):
        if (check_name is False) and (check_upc is False):
            print('hi')

            with open('data/data.json', 'r') as fr:
                data = json.loads(fr.read())

                for i, d in enumerate(data['product']):
                    if d['upc'] == self.upc and d['name'] == self.name:
                        data['product'].pop(i)
                        d['price'] = self.price
                        d['number'] = d['number'] + self.number
                        data['product'].append(d)
                        with open('data/data.json', 'w') as fw:
                            fw.write(json.dumps(data))
                        print(f'Your product is update.'
                              f' product name: {d["name"]}'
                              f' product upc: {d["upc"]}')

        elif check_upc is False and check_name is True:
            print(f'This UPC:{self.upc} is exist please try again...')

        elif check_name is False and check_upc is True:
            print(f'This name:{self.upc} is exist please try again...')

        elif check_upc and check_name:
            new_product = {
                "upc": self.upc,
                "name": self.name,
                "price": self.price,
                "number": self.number
            }

            return new_product

    def insert_to_file(self, new_product):
        if new_product is not None:
            with open('data/data.json', 'r') as fr:
                data = json.loads(fr.read())
                data['product'].append(new_product)

                with open('data/data.json', 'w') as fw:
                    fw.write(json.dumps(data))
                    print('Product add new product is: ', self.name)
