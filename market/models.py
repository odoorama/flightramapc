import uopy

class U2Message:

    def __init__(self):
        self.items = [
            {'id': 1, 'name': 'Flight', 'barcode': '893212299897', 'price': 500},
            {'id': 2, 'name': 'Flight', 'barcode': '123985473165', 'price': 1000},
            {'id': 3, 'name': 'Tour', 'barcode': '231985128446', 'price': 150},
            {'id': 4, 'name': 'Holiday', 'barcode': '231985128446', 'price': 750}
        ]
        self.planitems = [
            {'code': '1',
             'type': 'Transfer',
             'options': [{'description': 'From?', 'status': 'primary'},
                          {'description': 'To?', 'status': 'success'},
                          {'description': 'Date?', 'status': 'success'}
                          ],
              'actions': [{'description': 'add', 'status': 'primary'},
                          {'description': 'del', 'status': 'danger'}]
             },
            {'code': '2',
             'type': 'Flight',
              'options': [{'description': 'From?', 'status': 'primary'},
                          {'description': 'To?', 'status': 'success'},
                          {'description': 'Date?', 'status': 'success'}
                          ],
              'actions': [{'description': 'add', 'status': 'primary'},
                          {'description': 'del', 'status': 'danger'}
                          ]
             },
            {'code': '3',
             'type': 'Tour',
             'options': [{'description': 'Where?', 'status': 'primary'},
                         {'description': 'Date?', 'status': 'success'}],
             'actions': [{'description': 'add', 'status': 'primary'},
                         {'description': 'del', 'status': 'danger'}
                         ]
             },
            {'code': '4',
             'type': 'Hotel',
             'options': [{'description': 'Where?', 'status': 'primary'},
                         {'description': 'Date?', 'status': 'success'}
                         ],
             'actions': [{'description': 'add',
                          'status': 'primary'
                          },
                         {'description': 'del',
                          'status': 'danger'
                          }
                         ]
             }
        ]

    def get_items(self):
        return self.items

    def get_planitems(self):
        return self.planitems

#config = {}
#config['service'] = 'udcs'
#config['account'] = '/unidata/UNIRAMA'
#config['host'] = 't01.astratis.com'
#config['user'] = 'manos'
#config['password'] = 'ursos'
#config['port'] = 31438
#ain_U2_session = uopy.connect(**config)
#cmd = uopy.Command('SORT TAIRPORTS WITH @ID NE "//M" A1')
#cmd.run()
#print(cmd.response)
