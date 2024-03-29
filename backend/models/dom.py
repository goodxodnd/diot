#-*- coding:utf-8 -*-

import datetime
from flask import json

class Docu():
    """ 모든 Object Mapepr 클래스의 최상위 클래스

        Attributes:
        doc (dict): Mongo의 도큐먼트에 대응되는 값을 갖고 있는 dictionary.
        collection (str): 도큐먼트를 저장하는 컬렉션의 이름.

    """

    def __init__(self):
        self.doc = {}
        self.collection = None

    def to_json(self):
        """ 도큐먼트의 내용을 JSON으로 바꿔줌.
        Returns:
            str: json 문자열
        """
        return json.dumps(self.doc)

    def get_doc(self):
        """ 도큐먼트를 넘겨줌.
        Returns:
             dict: 도큐먼트 프로퍼티를 넘겨줌.
        """
        return self.doc


class User(Docu):
    """ 사용자 정보를 갖고 있는 Object Mapper """

    def __init__(self, did, email, logpass, gethpass, coreAccount, corePrvkey, corePubkey, user_dapp_addr):
        """ 초기화 함수
        Args:
            account (str): blockchain account
            did (str): 사용자 did
            email (str): 사용자 이메일
            logpass (str): 사용자의 로그인 패스워드
            gethpass (str): 사용자의 테스트넷 패스워드
       """
        super().__init__()
        self.collection = 'users'
        self.doc['did'] = did
        self.doc['email'] = email
        self.doc['logpass'] = logpass
        self.doc['gethpass'] = gethpass
        self.doc['coreAccount'] = coreAccount
        self.doc['corePrvkey'] = corePrvkey
        self.doc['corePubkey'] = corePubkey
        self.doc['user_dapp_addr'] = user_dapp_addr

    def get_account(self):
        """ 사용자 로그인 account를 반환
        Returns:
             str: account를 반환함.
        """
        return self.doc['account']


class DApp(Docu):
    """ DApp 정보를 갖고 있는 Object Mapper """

    def __init__(self, user, name, desc, abi, binary,contractAddress):
        """ 초기화 함수
        Args:
            user (User): DApp의 소유자
            dapp_name (str): dapp의 이름
            desc (str): dapp의 description.
            abi (str): dapp abi
            binary (str): dapp binary
            public (bool): 다른 사용자가 볼 수 있음. 디폴트는 false
       """
        super().__init__()
        self.collection = 'dapps'
        self.doc['user'] = user['_id']
        self.doc['name'] = name
        self.doc['desc'] = desc
        self.doc['abi'] = abi
        self.doc['bin'] = binary
        self.doc['upload_time'] = datetime.datetime.now()
        # add
        self.doc['contractAddress'] = contractAddress


class Device(Docu):
    """ Device DApp 정보를 갖고 있는 Object Mapper """

    def __init__(self, name, deviceType, info, did, publicKey, user_did , device_dapp_addr):
        """ 초기화 함수
        Args:
            user (User): DApp의 소유자
            deviceName (str): dapp의 이름
            desc (str): dapp의 description.
            public (bool): 다른 사용자가 볼 수 있음. 디폴트는 false
       """
        super().__init__()
        self.collection = 'device'
        self.doc['name'] = name
        self.doc['deviceType'] = deviceType
        self.doc['info'] = info
        self.doc['did'] = did
        self.doc['publicKey'] = publicKey
        self.doc['device_dapp_addr'] = device_dapp_addr
        self.doc['user_did'] = user_did
        self.doc['upload_time'] = datetime.datetime.now()


class Config(Docu):
    """ 사용자 정보를 갖고 있는 Object Mapper """

    def __init__(self, info,system_dapp_addr):
        """ 초기화 함수
        Args:
            system_dapp_addr (str): system_dapp_addr

       """
        super().__init__()
        self.collection = 'Config'
        self.doc['info'] = info
        self.doc['system_dapp_addr'] = system_dapp_addr


class Ticket(Docu):
    """ 사용자 정보를 갖고 있는 Object Mapper """

    def __init__(self, owner_ticket_addr, belongTo, user_dapp_addr):
        """ 초기화 함수
        Args:
            system_dapp_addr (str): system_dapp_addr

       """
        super().__init__()
        self.collection = 'ticket'
        self.doc['owner_ticket_addr'] = owner_ticket_addr
        self.doc['belongTo'] = belongTo
        self.doc['user_dapp_addr'] = user_dapp_addr
        self.doc['upload_time'] = datetime.datetime.now()


class EventRequest(Docu):
    """ Event 정보를 갖고 있는 Object Mapper """

    def __init__(self, _from, _to, _payload, _timestamp, event):
        """ 초기화 함수
        Args:
            system_dapp_addr (str): system_dapp_addr

       """
        super().__init__()
        self.collection = 'eventRequest'
        self.doc['_from'] = _from
        self.doc['_to'] = _to
        self.doc['_payload'] = _payload
        self.doc['event'] = event
        self.doc['done'] = False


class EventAccept(Docu):
    """ Event 정보를 갖고 있는 Object Mapper """

    def __init__(self, preOwner, newOwner, device):
        """ 초기화 함수
        Args:
            system_dapp_addr (str): system_dapp_addr

       """
        super().__init__()
        self.collection = 'eventAccept'
        self.doc['preOwner'] = preOwner
        self.doc['newOwner'] = newOwner
        self.doc['device'] = device
        self.doc['done'] = False