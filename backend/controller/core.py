from web3 import Web3, HTTPProvider
from backend.controller.config import CONFIG, ResCode, Mode, NetType
import json
from hexbytes import HexBytes
import base64
import hashlib
from Crypto.Cipher import AES
import os
from eth_account import Account
from eth_keys import keys
from backend.controller import dapp


class OwnershipManager():
    def __init__(self, core):
        self.core = core

    # It must be called before other method except "deploy_system_dapp()"
    def set_system_dapp(self, system_dapp_addr):
        self.system_dapp_addr = system_dapp_addr

    def deploy_system_dapp(self, account, gethpass='1234'):
        # Deploy User DApp
        params = {}
        params['account'] = account
        params['passwd'] = gethpass
        params['abi'] = dapp.SystemAbi
        params['bin'] = dapp.SystemBin
        ret = self.core.deployDApp(params)
        return ret

    def deploy_user_dapp(self, account, gethpass):
        # Deploy User DApp
        params = {}
        params['account'] = account
        params['passwd'] = gethpass
        params['abi'] = dapp.UserAbi
        params['bin'] = dapp.UserBin
        params['kwargs'] = {'_addrSystem': self.system_dapp_addr}
        ret = self.core.deployDApp(params)
        print(ret)
        return ret

    def deploy_device_dapp(self, owner_account, gethpass):
        # Device DApp
        params = {}
        params['account'] = owner_account
        params['passwd'] = gethpass
        params['abi'] = dapp.DeviceAbi
        params['bin'] = dapp.DeviceBin
        ret = self.core.deployDApp(params)
        print(ret)
        return ret

    def deploy_owner_ticket(self, owner_account, gethpass, user_dapp_addr, device_dapp_addr):
        # Owner Ticket DApp
        params = {}
        params['account'] = owner_account
        params['passwd'] = gethpass
        params['abi'] = dapp.OwnerTicketAbi
        params['bin'] = dapp.OwnerTicketBin
        kwargs = {'_userDAppAddr': user_dapp_addr}
        kwargs['_deviceDAppAddr'] = device_dapp_addr
        params['kwargs'] = kwargs
        ret = self.core.deployDApp(params)
        print(ret)
        return ret

    # the request from a user to claim the ownership
    def request_change_owner(self, account, gethpass, requester_dapp_addr, device_did, payload):
        params = {}
        params['account'] = account  # shoud be changed with a real account
        params['passwd'] = gethpass
        params['abi'] = dapp.UserAbi
        params['contractAddress'] = requester_dapp_addr
        params['functionName'] = 'sendRequest'
        params['kwargs'] = {'_deviceDID': device_did, '_payload': payload}

        ret = self.core.callTx(params)
        print(ret)
        return ret

    # change the ownership by the owner
    def change_owner(self, account, gethpass, user_dapp_addr, ticket_addr, user_did):
        params = {}
        params['account'] = account  # shoud be changed with a real account
        params['passwd'] = gethpass
        params['abi'] = dapp.UserAbi
        params['contractAddress'] = user_dapp_addr
        params['functionName'] = 'acceptRequest'
        params['kwargs'] = {'_addrTicket': ticket_addr, '_userDID': user_did}

        ret = self.core.callTx(params)
        print(ret)
        return ret

    def set_owner_ticket(self, account, gethpass, device_dapp_addr, owner_ticket_addr):
        params = {}
        params['account'] = account
        params['passwd'] = gethpass  # todo must setup this gethpath before running
        params['abi'] = dapp.DeviceAbi
        params['contractAddress'] = device_dapp_addr
        params['functionName'] = 'setOwnerTicket'
        kwargs = {}
        kwargs['_ticketAddr'] = owner_ticket_addr
        params['kwargs'] = kwargs

        return self.core.callTx(params)

    def register_member(self, did, eoa_addr, dapp_addr):
        # add did
        params = {}
        params['account'] = CONFIG['SYSTEM_EOA']
        params['passwd'] = CONFIG['SYSTEM_GETHPASS']  # todo must setup this gethpath before running
        params['abi'] = dapp.SystemAbi
        params['contractAddress'] = self.system_dapp_addr
        params['functionName'] = 'addMember'
        kwargs = {}
        kwargs['_did'] = did
        kwargs['_addrEOA'] = eoa_addr
        kwargs['_addrCA'] = dapp_addr
        params['kwargs'] = kwargs

        return self.core.callTx(params)

    def get_ca_addr(self, requester_dapp_addr, did):
        # Get CA Addr
        params = {}
        params['abi'] = dapp.SystemAbi
        params['account'] = requester_dapp_addr
        params['contractAddress'] = self.system_dapp_addr
        params['functionName'] = 'getCAAddr'
        params['kwargs'] = {'_did': did}

        ret = self.core.callFunction(params)
        return ret

class KeyManager():
    def __init__(self, passphrase="Raputa The Castle"):
        self.core = EthCore2(url=CONFIG['RPC-URL'], mode=Mode.PRODUCT)
        self.cipher = AESCipher(passphrase)

    def create_account(self, passphrase):
        acct = Account.create(passphrase)
        bkey = bytes(acct.key)
        hex_key = bkey.hex()
        print(hex_key)
        account = self.core.create_account_with_key(hex_key, passphrase)
        enc_prvkey = self.cipher.encrypt(hex_key)
        return account, enc_prvkey , hex_key

    def get_plainkey(self, enc_key):
        plain_key = self.cipher.decrypt(enc_key)
        return plain_key

    def get_pubkey(self, prvkey):
        b_prvkey = bytes.fromhex(prvkey)
        pk = keys.PrivateKey(b_prvkey)
        return pk.public_key

class AESCipher():
    def __init__(self, passphrase):
        self.bs = 32
        self.key = hashlib.sha256(AESCipher.str_to_bytes(passphrase)).digest()

    @staticmethod
    def str_to_bytes(data):
        u_type = type(b''.decode('utf8'))
        if isinstance(data, u_type):
            return data.encode('utf8')
        return data

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * AESCipher.str_to_bytes(chr(self.bs - len(s) % self.bs))

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    def encrypt(self, raw):
        raw = self._pad(AESCipher.str_to_bytes(raw))
        iv = os.urandom(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw)).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')


class EthCore2:
    '''
    Geth와 W3 통신을 하는 클래스임.
    '''

    def __init__(self, url, mode):
        self.mode = mode
        self.w3 = Web3(HTTPProvider(url))

    def create_account_with_key(self, prv_key, passwd):
        """ create account with private key
        Args:
            prv_key (str): hexstring private key
            passwd (str): user password

        Returns:
            str: the generated account
        """
        account = self.w3.geth.personal.import_raw_key(prv_key, passwd)
        return account

    # Account의 밸런스 값을 조회해서 넘겨주는 루틴
    def getBalance(self, params):
        balance = self.w3.eth.getBalance(
            self.w3.toChecksumAddress(params['account']))

        # retValue
        retValue = {'code': ResCode.OK.value}
        retValue['account'] = params['account']
        retValue['balance'] = balance

        return retValue

    def changeAddress(self, contract_address):
        return self.w3.toChecksumAddress(contract_address)

    # Get Block
    def getBlock(self, parameters):

        block_info = self.w3.eth.getBlock(parameters['blockNum'])
        ret_info = {}
        for k in block_info:
            if isinstance(block_info[k], list):
                items = []
                for item in block_info[k]:
                    if isinstance(item, HexBytes):
                        items.append(item.hex())
                    else:
                        items.append(item)
                ret_info[k] = items
            elif isinstance(block_info[k], HexBytes):
                ret_info[k] = block_info[k].hex()
            else:
                ret_info[k] = block_info[k]
        print(ret_info)

        retValue = {'code': ResCode.OK.value}
        retValue['blockInfo'] = ret_info
        return retValue

    # Get Tx
    def getTx(self, parameters):

        ret_info = {}
        tx_info = self.w3.eth.getTransaction(parameters['txHash'])
        if tx_info:
            for k in tx_info:
                if isinstance(tx_info[k], HexBytes):
                    ret_info[k] = tx_info[k].hex()
                else:
                    ret_info[k] = tx_info[k]
            print(ret_info)
        else:
            ret_info['txInfo'] = 'None'

        retValue = {'code': ResCode.OK.value}
        retValue['txInfo'] = ret_info
        return retValue


    # Function를 호출함. Call Function임.
    def callFunction(self, params):

        # 해당 사용자의 패스워드를 이용해서 Unlock 함.
        if self.mode != Mode.DEV:
            self.w3.geth.personal.unlockAccount(self.w3.toChecksumAddress(
                params['account']), params['passwd'], 0)

        # # 원래는 바이트 이어야 하므로 hex 값에서 바이트 코드로 변경
        # tx_hash = bytes.fromhex(parameters['txHash'])
        #
        # # receipt get
        # tx_receipt = self.w3.eth.getTransactionReceipt(tx_hash)

        # contract의 주소를 얻음.
        contract_address = params['contractAddress']

        # abi 인터페이스,
        abi = json.loads(params['abi'])

        # Contract 인스턴스를 생성
        contract_instance = self.w3.eth.contract(
            address=contract_address,
            abi=abi
        )

        # 함수를 이름을 이용해서 함수 객체를 얻음
        funx = contract_instance.functions[params['functionName']]
        # result = contract_instance.functions.greet().call()
        # func = getattr(contract_instance.call(), parameters['functionName'])
        # print(contract_instance.call())
        # print('Contract: {}'.format(contract_instance.call().greet()))

        # get parameters
        if 'kwargs' in params:
            kwargs = params['kwargs']
            result = funx(**kwargs).call({'from': self.w3.toChecksumAddress(params['account'])})
        else:
            result = funx().call({'from': self.w3.toChecksumAddress(params['account'])})

        print(result)
        # 현재는 그냥 100% 성공이라고 했음.
        # 실제로는 에러 처리 코드가 필요함
        retValue = {'code': ResCode.OK.value}
        retValue['return'] = result
        print(retValue)

        return retValue

    # Method를 호출함. Tx Method .
    def callTx(self, params):

        # 해당 사용자의 패스워드를 이용해서 Unlock 함.
        if self.mode != Mode.DEV:
            self.w3.geth.personal.unlockAccount(self.w3.toChecksumAddress(
                params['account']), params['passwd'], 0)

        # # 원래는 바이트 이어야 하므로 hex 값에서 바이트 코드로 변경
        # tx_hash = bytes.fromhex(parameters['txHash'])
        #
        # # receipt get
        # tx_receipt = self.w3.eth.getTransactionReceipt(tx_hash)

        # contract의 주소를 얻음.
        contract_address = self.w3.toChecksumAddress(params['contractAddress'])

        # abi 인터페이스,
        abi = json.loads(params['abi'])

        # Contract 인스턴스를 생성
        contract_instance = self.w3.eth.contract(
            address=contract_address,
            abi=abi
        )

        # 함수를 이름을 이용해서 함수 객체를 얻음
        # funx = contract_instance.find_functions_by_name(parameters['functionName'])
        # print(funx)
        funx = contract_instance.functions[params['functionName']]
        # result = contract_instance.functions.greet().call()
        # func = getattr(contract_instance.call(), parameters['functionName'])
        # print(contract_instance.call())
        # print('Contract: {}'.format(contract_instance.call().greet()))

        # get parameters
        if 'kwargs' in params:
            kwargs = params['kwargs']
            txhash = funx(**kwargs).transact({'from': self.w3.toChecksumAddress(params['account'])})
        else:
            print('No arguments')
            txhash= funx().transact({'from': self.w3.toChecksumAddress(params['account'])})

        tx_receipt = self.w3.eth.waitForTransactionReceipt(txhash)
        print('receipt', tx_receipt)
        # 현재는 그냥 100% 성공이라고 했음.
        # 실제로는 에러 처리 코드가 필요함
        retValue = {'code': ResCode.OK.value}
        retValue['return'] = 'success'
        return retValue


    # DApp을 Deployment

    def deployDApp(self, params):

        self.w3.eth.defaultAccount = self.w3.toChecksumAddress(params['account'])

        # 해당 사용자의 패스워드를 이용해서 Unlock 함.
        if self.mode != Mode.DEV:
            self.w3.geth.personal.unlockAccount(self.w3.toChecksumAddress(
                params['account']), params['passwd'], 0)

        # contract 생성
        contract = self.w3.eth.contract(abi=params['abi'], bytecode=params['bin'])

        # get parameters
        if 'kwargs' in params:
            kwargs = params['kwargs']
            tx_hash = contract.constructor(**kwargs).transact()
        else:
            tx_hash = contract.constructor().transact()

        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)

        contract_address = tx_receipt['contractAddress']

        # deploy 요청에 의거한 tx hash
        # tx_hash = contract.deploy(
        #     transaction={'from': self.w3.toChecksumAddress(parameters['account'])})
        # print("tx_hash: {}".format(tx_hash.hex()))
        # print("Finish Deploying")
        #
        # # 블록이 채굴되기 전에 바로 contract를 요청할 수 없으므로, 기다려야 함.
        # while True:
        #     # 블록에서 hash가 들어있는 블록이 있는지 요청
        #     tx_receipt = self.w3.eth.getTransactionReceipt(tx_hash)
        #
        #     # 아직 채굴 전
        #     if tx_receipt is None:
        #         time.sleep(1)
        #         print("waiting")
        #         continue
        #
        #     # 채굴 완료
        #     print(tx_receipt)
        #     contract_address = tx_receipt['contractAddress']
        #     print(contract_address)
        #
        #     break

        # 현재는 그냥 100% 성공이라고 했음.
        # 실제로는 에러 처리 코드가 필요함
        ret_info = {}
        if tx_receipt:
            for k in tx_receipt:
                if isinstance(tx_receipt[k], HexBytes):
                    ret_info[k] = tx_receipt[k].hex()
                else:
                    ret_info[k] = tx_receipt[k]
            print(ret_info)
        else:
            ret_info['txInfo'] = 'None'

        retValue = {'code': ResCode.OK.value}
        retValue['deployResult'] = ret_info
        print(retValue)

        return retValue


    # Account를 생성
    def createAccount(self, parameters):

        # 해당 사용자의 패스워드를 이용해서 Unlock 함.
        addr = self.w3.geth.personal.newAccount(parameters['password'])

        # 현재는 그냥 100% 성공이라고 했음.
        # 실제로는 에러 처리 코드가 필요함
        retValue = {'code': ResCode.OK.value}
        if isinstance(addr, HexBytes):
            retValue['accountAddr'] = addr.hex()
        else:
            retValue['accountAddr'] = addr

        return retValue

    # Account를 생성

    def fillEth(self, parameters):

        # unlock Adam's pass
        adam_account = self.w3.toChecksumAddress(CONFIG['ADAM'])
        self.w3.geth.personal.unlockAccount(adam_account, 'yes36%')

        args = {}
        args['to'] = self.w3.toChecksumAddress(parameters['to'])
        args['from'] = adam_account
        args['value'] = parameters['amount']* pow(10 ,18)

        # 해당 사용자의 패스워드를 이용해서 Unlock 함.
        tx_addr = self.w3.eth.sendTransaction(args)
        print(tx_addr)

        self.w3.eth.waitForTransactionReceipt(tx_addr)

        balance = self.w3.eth.getBalance(args['to'] )

        # retValue
        # 현재는 그냥 100% 성공이라고 했음.
        # 실제로는 에러 처리 코드가 필요함
        retValue = {'code': ResCode.OK.value}
        retValue['balance'] = balance

        return retValue


class EthCore:
    '''
    Geth와 W3 통신을 하는 클래스임.
    '''

    def __init__(self, url=CONFIG['GANACHE'], net=NetType.GANACHE):
        self.net = net
        self.w3 = Web3(HTTPProvider(url))

    # Account의 밸런스 값을 조회해서 넘겨주는 루틴
    def getBalance(self, parameters):
        balance = self.w3.eth.getBalance(
            self.w3.toChecksumAddress(parameters['account']))

        # retValue
        retValue = {'code': ResCode.OK.value}
        retValue['account'] = parameters['account']
        retValue['balance'] = balance

        return retValue


    # Get Block
    def getBlock(self, payload):
        # 파라미터를 먼저 얻음.
        parameters = payload['params']

        block_info = self.w3.eth.getBlock(parameters['blockNum'])
        ret_info = {}
        for k in block_info:
            if isinstance(block_info[k], list):
                items = []
                for item in block_info[k]:
                    if isinstance(item, HexBytes):
                        items.append(item.hex())
                    else:
                        items.append(item)
                ret_info[k] = items
            elif isinstance(block_info[k], HexBytes):
                ret_info[k] = block_info[k].hex()
            else:
                ret_info[k] = block_info[k]
        print(ret_info)

        retValue = {'code': ResCode.OK.value}
        retValue['blockInfo'] = ret_info
        return retValue

    # Get Tx
    def getTx(self, payload):
        # 파라미터를 먼저 얻음.
        parameters = payload['params']

        ret_info = {}
        tx_info = self.w3.eth.getTransaction(parameters['txHash'])
        if tx_info:
            for k in tx_info:
                if isinstance(tx_info[k], HexBytes):
                    ret_info[k] = tx_info[k].hex()
                else:
                    ret_info[k] = tx_info[k]
            print(ret_info)
        else:
            ret_info['txInfo'] = 'None'

        retValue = {'code': ResCode.OK.value}
        retValue['txInfo'] = ret_info
        return retValue


    # Function를 호출함. Call Function임.
    def callFunction(self, parameters):

        # 해당 사용자의 패스워드를 이용해서 Unlock 함.
        if self.net != Mode.GANACHE:
            self.w3.geth.personal.unlockAccount(self.w3.toChecksumAddress(
                parameters['account']), parameters['gethpass'], 0)

        # # 원래는 바이트 이어야 하므로 hex 값에서 바이트 코드로 변경
        # tx_hash = bytes.fromhex(parameters['txHash'])
        #
        # # receipt get
        # tx_receipt = self.w3.eth.getTransactionReceipt(tx_hash)

        # contract의 주소를 얻음.
        contract_address = parameters['contractAddress']

        # abi 인터페이스,
        abi = json.loads(parameters['abi'])

        # Contract 인스턴스를 생성
        contract_instance = self.w3.eth.contract(
            address=contract_address,
            abi=abi
        )

        # 함수를 이름을 이용해서 함수 객체를 얻음
        funx = contract_instance.functions[parameters['functionName']]
        # result = contract_instance.functions.greet().call()
        # func = getattr(contract_instance.call(), parameters['functionName'])
        # print(contract_instance.call())
        # print('Contract: {}'.format(contract_instance.call().greet()))

        # get parameters
        if 'kwargs' in parameters:
            kwargs = parameters['kwargs']
            result = funx(**kwargs).call()
        else:
            result = funx().call()

        print(result)
        # 현재는 그냥 100% 성공이라고 했음.
        # 실제로는 에러 처리 코드가 필요함
        retValue = {'code': ResCode.OK.value}
        retValue['return'] = result

        return retValue

    # Method를 호출함. Tx Method .
    def callTx(self, parameters):

        if self.net != NetType.GANACHE:
            # 해당 사용자의 패스워드를 이용해서 Unlock 함.
            self.w3.geth.personal.unlockAccount(self.w3.toChecksumAddress(
                parameters['account']), parameters['gethpass'], 0)

        # # 원래는 바이트 이어야 하므로 hex 값에서 바이트 코드로 변경
        # tx_hash = bytes.fromhex(parameters['txHash'])
        #
        # # receipt get
        # tx_receipt = self.w3.eth.getTransactionReceipt(tx_hash)

        # contract의 주소를 얻음.
        contract_address = self.w3.toChecksumAddress(parameters['contractAddress'])

        # abi 인터페이스,
        abi = json.loads(parameters['abi'])

        # Contract 인스턴스를 생성
        contract_instance = self.w3.eth.contract(
            address=contract_address,
            abi=abi
        )

        # 함수를 이름을 이용해서 함수 객체를 얻음
        # funx = contract_instance.find_functions_by_name(parameters['functionName'])
        # print(funx)
        funx = contract_instance.functions[parameters['functionName']]
        # result = contract_instance.functions.greet().call()
        # func = getattr(contract_instance.call(), parameters['functionName'])
        # print(contract_instance.call())
        # print('Contract: {}'.format(contract_instance.call().greet()))

        # get parameters
        if 'kwargs' in parameters:
            kwargs = parameters['kwargs']
            txhash = funx(**kwargs).transact({'from': self.w3.toChecksumAddress(parameters['account'])})
        else:
            print('No arguments')
            txhash= funx().transact({'from': self.w3.toChecksumAddress(parameters['account'])})

        tx_receipt = self.w3.eth.waitForTransactionReceipt(txhash)
        print('receipt', tx_receipt)
        # 현재는 그냥 100% 성공이라고 했음.
        # 실제로는 에러 처리 코드가 필요함
        retValue = {'code': ResCode.OK.value}
        retValue['return'] = 'success'
        return retValue


    # get public key
    def getPublicKey(self, params):
        self.w3.eth.defaultAccount = self.w3.toChecksumAddress(params['account'])
        print(self.w3.eth.defaultAccount)

    # DApp을 Deployment
    def deployDApp(self, payload):
        # 파라미터를 먼저 얻음.
        parameters = payload['params']

        self.w3.eth.defaultAccount = self.w3.toChecksumAddress(parameters['account'])

        # 해당 사용자의 패스워드를 이용해서 Unlock 함.
        self.w3.geth.personal.unlockAccount(self.w3.toChecksumAddress(
            parameters['account']), parameters['passwd'], 0)

        # contract 생성
        print(type(parameters['bin']), ":", parameters['bin'])
        contract = self.w3.eth.contract(abi=parameters['abi'], bytecode=parameters['bin'])

        tx_hash = contract.constructor().transact()

        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)

        # contract_address = tx_receipt['contractAddress']

        # deploy 요청에 의거한 tx hash
        # tx_hash = contract.deploy(
        #     transaction={'from': self.w3.toChecksumAddress(parameters['account'])})
        # print("tx_hash: {}".format(tx_hash.hex()))
        # print("Finish Deploying")
        #
        # # 블록이 채굴되기 전에 바로 contract를 요청할 수 없으므로, 기다려야 함.
        # while True:
        #     # 블록에서 hash가 들어있는 블록이 있는지 요청
        #     tx_receipt = self.w3.eth.getTransactionReceipt(tx_hash)
        #
        #     # 아직 채굴 전
        #     if tx_receipt is None:
        #         time.sleep(1)
        #         print("waiting")
        #         continue
        #
        #     # 채굴 완료
        #     print(tx_receipt)
        #     contract_address = tx_receipt['contractAddress']
        #     print(contract_address)
        #
        #     break

        # 현재는 그냥 100% 성공이라고 했음.
        # 실제로는 에러 처리 코드가 필요함
        ret_info = {}
        if tx_receipt:
            for k in tx_receipt:
                if isinstance(tx_receipt[k], HexBytes):
                    ret_info[k] = tx_receipt[k].hex()
                else:
                    ret_info[k] = tx_receipt[k]
            print(ret_info)
        else:
            ret_info['txInfo'] = 'None'

        retValue = {'code': ResCode.OK.value}
        retValue['deployResult'] = ret_info
        print(retValue)

        return retValue


    # Account를 생성
    def createAccount(self, parameters):
        # 파라미터를 먼저 얻음.

        # 해당 사용자의 패스워드를 이용해서 Unlock 함.
        addr = self.w3.geth.personal.newAccount(parameters['password'])

        # 현재는 그냥 100% 성공이라고 했음.
        # 실제로는 에러 처리 코드가 필요함
        retValue = {'code': ResCode.OK.value}
        if isinstance(addr, HexBytes):
            retValue['accountAddr'] = addr.hex()
        else:
            retValue['accountAddr'] = addr

        return retValue

    # Account를 생성

    def fillEth(self, payload):

        # unlock Adam's pass
        adam_account = self.w3.toChecksumAddress(CONFIG['ADAM'])
        self.w3.geth.personal.unlockAccount(adam_account, 'yes36%')

        # 파라미터를 먼저 얻음.
        parameters = payload['params']

        args = {}
        args['to'] = self.w3.toChecksumAddress(parameters['to'])
        args['from'] = adam_account
        args['value'] = parameters['amount']* pow(10 ,18)

        # 해당 사용자의 패스워드를 이용해서 Unlock 함.
        tx_addr = self.w3.eth.sendTransaction(args)
        print(tx_addr)

        self.w3.eth.waitForTransactionReceipt(tx_addr)

        balance = self.w3.eth.getBalance(args['to'] )

        # retValue
        # 현재는 그냥 100% 성공이라고 했음.
        # 실제로는 에러 처리 코드가 필요함
        retValue = {'code': ResCode.OK.value}
        retValue['balance'] = balance

        return retValue
