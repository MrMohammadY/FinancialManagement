import json
from Data import Data


class EditProduct:
    def __init__(self, upc, name, new_upc, new_name, new_price, new_number):
        self.upc = upc
        self.name = name
        self.new_upc = new_upc
        self.new_name = new_name
        self.new_price = new_price
        self.new_number = new_number

    def edit_pro(self):

        with open('data/data.json', 'r') as fr:
            data = json.loads(fr.read())

            for index, pro in enumerate(data['product']):
                if pro['upc'] == self.upc and pro['name'] == self.name:
                    check = Data(self.new_upc, self.new_name,
                                 self.new_price, self.new_number)

                    if check.check_upc() is False:
                        data['product'].pop(index)

                        pro['upc'] = self.new_upc
                        pro['name'] = self.new_name
                        pro['price'] = self.new_price
                        pro['number'] = self.new_number

                        data['product'].append(pro)
                        with open('data/data.json', 'w') as fw:
                            fw.write(json.dumps(data))
                        print('updated')
                    else:
                        print('upc is not exist!!!!!!!')


class DeleteProduct:

    def __init__(self, upc, name):
        self.upc = upc
        self.name = name

    def delete(self):

        with open('data/data.json', 'r') as fr:
            data = json.loads(fr.read())
            if len(data['product']) == 1:
                print('you can\'t delete because has one product')
            else:
                for index, pro in enumerate(data['product']):
                    if pro['upc'] == self.upc and pro['name'] == self.name:
                        data['product'].pop(index)

            with open('data/data.json', 'w') as fw:
                fw.write(json.dumps(data))
                print('deleted!')
