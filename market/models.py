import uopy
import json
from json import JSONEncoder
from market import bcrypt
from market import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.load_user(user_id)


class User(UserMixin):

    def __init__(self, username, email_address, password):
        self.id = ''
        self.username = username
        self.email_address = email_address
#        self.password_hash = password_hash
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')


    def newuser(self):
        runflags = '1'
        userJSONData = json.dumps(self, indent=4, cls=GeneralEncoder)
        runmsgs = userJSONData
        ret_arrays = UopyMessage.sendmessage(runflags, runmsgs)

    def load_user(self, user_id):
        runflags = '2'
        self.id = user_id
        userJSONData = json.dumps(self, indent=4, cls=GeneralEncoder)
        runmsgs = userJSONData
        ret_arrays = UopyMessage.sendmessage(runflags, runmsgs)
        userJSONData = ret_arrays[2][1]
        dict_user = json.loads(userJSONData)
        self.id = dict_user['id']
        self.username = dict_user['username']
        self.email_address = dict_user['email_address']
        self.password_hash = dict_user['password_hash']
        return self

class GeneralEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class U2Message:

    def __init__(self):
        flight_stage = {'stage_type': 'Flight', 'stage_principal': 'Air France', 'stage_principal_logo': 'AF.png'}
        accom_stage = {'stage_type': 'Hotel', 'stage_principal': 'Hilton', 'stage_principal_logo': 'AF.png'}
        itineraryF = [flight_stage, flight_stage]
        itineraryA = []

        self.product_list = [
            {'id': 1, 'type': 'Flight', 'name': 'Flight London - Accra', 'barcode': '893212299897', 'price': 500,
             'itinerary': itineraryF},
            {'id': 2, 'type': 'Flight', 'name': 'Flight Only Accra - London', 'barcode': '123985473165', 'price': 1000,
             'itinerary': itineraryF},
            {'id': 3, 'type': 'Tour', 'name': 'Best of Accra Ten Days', 'barcode': '231985128446', 'price': 150,
             'itinerary': itineraryA},
            {'id': 4, 'type': 'Holiday', 'name': 'Beach Holiday Smithtown', 'barcode': '231985128446', 'price': 750,
             'itinerary': itineraryA}
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

    def get_product_list(self):
        return self.product_list

    def get_planitems(self):
        return self.planitems


class UopyMessage:

    @classmethod
    def sendmessage(cls, runflags, runmsgs):

        config = {}
        config['service'] = 'udcs'
        config['account'] = '/unidata/UNIRAMA'
        config['host'] = 't01.astratis.com'
        config['user'] = 'manos'
        config['password'] = 'ursos'
        config['port'] = 31438

        try:
            with uopy.connect(**config):
                sub = uopy.Subroutine('TS_UOPY_MSG', 5)
                sub.args[0] = runflags
                sub.args[1] = runmsgs
                sub.args[2] = ''
                sub.args[3] = ''
                sub.args[4] = ''
                sub.call()
                return sub.args
        except:
            print('try failed')
            return []


#main_U2_session = uopy.connect(**config)
#cmd = uopy.Command('SORT TAIRPORTS WITH @ID NE "//M" A1')
#cmd.run()
#print(cmd.response)
