from bson import json_util
from flask import Blueprint,request,Response,jsonify
from datetime import timedelta, datetime
from functools import wraps
import json
import jwt
from backend.models.dom import User
from backend.models.dom import Device
from backend.models.dom import DApp, Ticket

from backend.controller.config import CONFIG, Mode, ResCode

api_page = Blueprint('api_page',__name__)
api_page.resource = {'JWT_SECRET_KEY': '8akdjfl*#Q@OS)_Dkljdlkdja'}


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(request.headers)
        access_token = request.headers.get('Authorization')
        if access_token is not None:
            try:
                payload = jwt.decode(access_token, api_page.resource['JWT_SECRET_KEY'], 'HS256')
            except jwt.InvalidTokenError as ex:
                payload = None
                print(ex)

            if payload is None:
                print('111')
                return Response(status=401)

            did = payload['did']
            kwargs['did'] = did
        else:
            print('222')
            return Response(status=401)

        return f(*args, **kwargs)

    return decorated_function


@api_page.route('/register', methods=['POST'])
def register():
    # get parameters
    did = request.json['did']
    email = request.json['Email']
    logpass = request.json['password']
    gethpass = logpass + 'xaaa'

    user_info = api_page.resource['mongo'].find_user_by_did(did)
    if user_info['code'] == 200:
        # Same Did in Mongo
        return jsonify({
            'a-code': 404
        })
    else:
        # core Account Creation
        coreAccount, corePrvkey = api_page.resource['key_manager'].create_account(logpass)

        print(coreAccount, corePrvkey)

        # Fill eth
        params = {
            "to": coreAccount,
            "amount": 5
        }

        result = api_page.resource['core'].fillEth(params)
        print(result)

        # Deploy user dapp
        ret = api_page.resource['ownership_manager'].deploy_user_dapp(coreAccount, gethpass=logpass)
        if ret['code'] == ResCode.OK.value:
            user_dapp_addr = ret['deployResult']['contractAddress']
            print('b',user_dapp_addr)

        # register member
        ret = api_page.resource['ownership_manager'].register_member(did, coreAccount, user_dapp_addr)
        if ret['code'] != ResCode.OK.value:
            print(ret)
            exit(-1)
        else:
            print('well done')

        # get account addr
        user = User(did, email, logpass, gethpass, coreAccount, corePrvkey,user_dapp_addr)
        print('c', user)

        # add user to db
        mongoResult = api_page.resource['mongo'].add_user(user)
        response = json.dumps(mongoResult, default=json_util.default)
        return response


@api_page.route('/signin', methods=['POST'])
def login():
    login_did = request.json['did']
    # login_pwd = bcrypt.hashpw(request.json['password'].encode('UTF-8'), bcrypt.gensalt())
    login_pwd = request.json['password'].encode('UTF-8')
    login_pass = login_pwd.decode('ascii')

    print(login_did)

    # get a hash pwd from the given pwd
    # hashed_pwd = bcrypt.hashpw(login_pwd, bcrypt.gensalt())

    # compare it with DB
    result = api_page.resource['mongo'].auth_user_by_did(login_did, login_pass)

    print(result)
    if result['code'] == 200:
        # check DB (System dapp develope)

        # ret = ownership_manager.deploy_system_dapp(CONFIG['SYSTEM_EOA'])
        # if ret['code'] == ResCode.OK.value:
        #     system_dapp_addr = ret['deployResult']['contractAddress']
        #     ownership_manager.set_system_dapp(system_dapp_addr)

        # Login Success
        payload = {
            'did': login_did,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60)
        }

        # User Dapp Deployment -> (example) John
        # ret = ownership_manager.deploy_user_dapp(CONFIG['JOHN_EOA'], system_dapp_addr)
        # if ret['code'] == ResCode.OK.value:
        #     john_dapp_addr = ret['deployResult']['contractAddress']

        token = jwt.encode(payload, api_page.resource['JWT_SECRET_KEY'], 'HS256')
        return jsonify({
            'code': 200,
            'access_token': token.decode('UTF-8')
        })
    else:
        # Login Fail
        return jsonify({
            'code': 404
        })


@api_page.route('/getUserInfo', methods=['GET'])
@login_required
def getUserInfo(*args, **kwargs):
    did = request.headers.get('did')

    user_info = api_page.resource['mongo'].find_user_by_did(did)
    if user_info['code'] == 200:

        # get params
        print(user_info)

        payload = user_info['payload']

        return payload

    else:
        return user_info


@api_page.route('/getDeviceInfo', methods=['GET'])
@login_required
def getDeviceInfo(*args, **kwargs):
    did = request.headers.get('did')

    device_info = api_page.resource['mongo'].find_other_Device_did(did)
    print('deviceinfo', device_info)

    result = device_info["payload"]

    response = json.dumps(result, default=json_util.default)
    print('DEVICE response', response)
    return response


@api_page.route('/getMyDeviceList', methods=['GET'])
@login_required
def getMyDeviceList(*args, **kwargs):
    did = request.headers.get('did')

    myDeviceInfo = api_page.resource['mongo'].find_Mydevice_did(did)
    print('My device',myDeviceInfo)

    response = json.dumps(myDeviceInfo, default=json_util.default)
    return response


@api_page.route('/fill_eth', methods=['GET'])
@login_required
def fill_eth(*args, **kwargs):
    did = request.headers.get('did')

    user_info = api_page.resource['mongo'].find_user_by_did(did)
    if user_info['code'] == 200:
        # get params
        params = {
                "to": user_info['payload']['coreAccount'],
                "amount": 5
            }

        payload = {"params": params}

        # call core
        result = api_page.resource['core'].fillEth(params)
        response = json.dumps(result, default=json_util.default)
        return response
        print(response)
    else:
        return user_info


@api_page.route('/balance', methods=['GET'])
@login_required
def getbalance(*args, **kwargs):
    did = request.headers.get('did')

    user_info = api_page.resource['mongo'].find_user_by_did(did)

    if user_info['code'] == 200:

        # get params
        print(user_info)

        payload = user_info['payload']
        parameters = { }
        parameters['account'] = payload['coreAccount']

        # call core
        result = api_page.resource['core'].getBalance(parameters)
        response = json.dumps(result, default=json_util.default)
        print(response)
        return response
    else:
        return user_info

@api_page.route('/add_device', methods=['GET', 'POST'])
def add_device():
    name = request.json['name']
    deviceType = request.json['deviceType']
    info = request.json['info']
    did = request.json['did']
    publicKey = request.json['publicKey']
    UserDid = request.json['didName']

    print('c', UserDid)
    user_info = api_page.resource['mongo'].find_user_by_did(UserDid)

    UserEoa = user_info['payload']['coreAccount']
    UserPass = user_info['payload']['logpass']
    User_dapp_addr = user_info['payload']['user_dapp_addr']
    user_did = user_info['payload']['did']

    # 3. Device Dapp Deployment
    ret = api_page.resource['ownership_manager'].deploy_device_dapp(UserEoa, UserPass)
    if ret['code'] == ResCode.OK.value:
        device_dapp_addr = ret['deployResult']['contractAddress']
        print(device_dapp_addr)

    # 4. Register DApps
    ret = api_page.resource['ownership_manager'].register_member(did, UserEoa, device_dapp_addr)
    if ret['code'] != ResCode.OK.value:
        print(ret)
        exit(-1)
    print('register DApp well done.')

    device = Device(name, deviceType, info, did, publicKey,user_did, device_dapp_addr)
    print('a-3', device)

    mongoResult = api_page.resource['mongo'].add_device(device)
    print(mongoResult)
    response = json.dumps(mongoResult, default=json_util.default)

    # 6. Owner Ticket Deployment
    ret = api_page.resource['ownership_manager'].deploy_owner_ticket(UserEoa, UserPass, User_dapp_addr, device_dapp_addr)
    if ret['code'] == ResCode.OK.value:
        owner_ticket_addr = ret['deployResult']['contractAddress']
        print(owner_ticket_addr)

    belongTo = UserDid
    user_dapp_addr = User_dapp_addr

    ticket = Ticket(owner_ticket_addr,belongTo,user_dapp_addr)
    ticketResult = api_page.resource['mongo'].add_ticket(ticket)
    print('t', ticketResult)

    # 7. set the owner ticket to device
    ret = api_page.resource['ownership_manager'].set_owner_ticket(UserEoa, UserPass, device_dapp_addr, owner_ticket_addr)
    if ret['code'] == ResCode.OK.value:
        print('owner ticket well')
    return response


# TODO ownerRequest
@api_page.route('/request_owner', methods=['POST'])
def request_owner():
    UserDid = request.json['didName']
    DeviceDid = request.json['Did']

    user_info = api_page.resource['mongo'].find_user_by_did(UserDid)

    UserEoa = user_info['payload']['coreAccount']
    UserPass = user_info['payload']['logpass']
    User_dapp_addr = user_info['payload']['user_dapp_addr']

    # 8. Change Request. (Bob to John)
    ret = api_page.resource['ownership_manager'].request_change_owner(UserEoa, UserPass, User_dapp_addr, DeviceDid, UserDid)
    if ret['code'] == ResCode.OK.value:
        print('well')

    return ret


@api_page.route('/find_event', methods=['GET'])
def find_event():
    did = request.headers.get('did')
    print('did', did)

    user_info = api_page.resource['mongo'].find_user_by_did(did)
    device_all_info = api_page.resource['mongo'].find_device_by_did(did)

    user_dapp_addr = user_info['payload']['user_dapp_addr']

    print('user_dapp_addr', user_dapp_addr)
    print('device_info', device_all_info)
    device_name = device_all_info['payload']['name']
    device_info = device_all_info['payload']['info']
    device_did = device_all_info['payload']['did']

    user_event_request = api_page.resource['mongo'].find_EventRequest_by_DappAddr(user_dapp_addr)
    print('user_event_request!', user_event_request )
    _payload = user_event_request['payload']['_payload']

    result = {'device_name': device_name, 'device_info': device_info,'device_did': device_did , 'RequestUserName': _payload , 'UserName' : did}

    print(result)

    response = json.dumps(result, default=json_util.default)
    print('event response', response)

    return response


@api_page.route('/checkOwnerShip', methods=['GET'])
def checkOwnerShip():
    did = request.headers.get('did')
    print('did:', did)

    user_info = api_page.resource['mongo'].find_user_by_did(did)

    user_dapp_addr = user_info['payload']['user_dapp_addr']

    user_event_request = api_page.resource['mongo'].find_EventRequest_by_DappAddr(user_dapp_addr)

    if user_event_request['code'] == 404:

        print('none request')

        return jsonify('none request')

    else:

        _payload = user_event_request['payload']['_payload']
        event = user_event_request['payload']['event']

        result = {'RequestUserName': _payload, 'UserName': did, 'event': event}

        print('result:', result)

        response = json.dumps(result, default=json_util.default)

        return response


@api_page.route('/checkOwnerShipAccept', methods=['GET'])
def checkOwnerShipAccept():
    did = request.headers.get('did')
    print('did:', did)

    user_info = api_page.resource['mongo'].find_user_by_did(did)

    user_dapp_addr = user_info['payload']['user_dapp_addr']

    user_event_request = api_page.resource['mongo'].find_EventAccept_by_DappAddr(user_dapp_addr)

    if user_event_request['code'] == 404:

        print('none accept')

        return jsonify('none accept')

    else:

        return jsonify('accpet done')


@api_page.route('/change_owner', methods=['POST'])
def change_owner():
    UserDid = request.json['didName']
    DeviceName = request.json['DeviceName']
    RequestUserName = request.json['RequestUserName']
    print('userdid', UserDid)

    user_info = api_page.resource['mongo'].find_user_by_did(UserDid)

    UserEoa = user_info['payload']['coreAccount']
    UserPass = user_info['payload']['logpass']
    User_dapp_addr = user_info['payload']['user_dapp_addr']

    user_event_request = api_page.resource['mongo'].find_EventRequest_by_DappAddr(User_dapp_addr)
    print('user-event', user_event_request)
    _payload = user_event_request['payload']['_payload']

    # new user info
    new_user_info = api_page.resource['mongo'].find_user_by_did(_payload)
    new_user_dapp_addr = new_user_info['payload']['user_dapp_addr']


    ticket_info = api_page.resource['mongo'].find_ticket_by_did(UserDid)
    print('t', ticket_info)
    owner_ticket_addr = ticket_info['payload']['owner_ticket_addr']

    # Change DB Device
    change_info = api_page.resource['mongo'].update_one(UserDid, _payload)
    print('change info', change_info)

    # Change DB request boolean (False -> True)
    change_request = api_page.resource['mongo'].update_request()
    print('change_request_boolean', change_request)

    # Change Ticket
    ticket_change = api_page.resource['mongo'].ticket_update(UserDid, _payload, new_user_dapp_addr)
    print('ticket', ticket_change)

    # 9-1. Change Owner. (Bob -> John)
    ret = api_page.resource['ownership_manager'].change_owner(UserEoa, UserPass , User_dapp_addr, owner_ticket_addr, RequestUserName)
    if ret['code'] == ResCode.OK.value:
        print('well')

    print('r', ret)

    return ret

