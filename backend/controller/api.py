from flask import Blueprint,request,Response,jsonify
import json
from bson import json_util
from backend.models.dom import User
from backend.models.database import ZenMongo
from pymongo import MongoClient, collection


api_page = Blueprint('api_page',__name__)
api_page.resource = {'JWT_SECRET_KEY': '8akdjfl*#Q@OS)_Dkljdlkdja'}


@api_page.route('/tiki', methods=["GET", "POST"])
def tiki_taka():
    return("taka")


@api_page.route('/register', methods=['POST'])
def register():
    # get parameters
    did = request.json['did']
    email = request.json['Email']
    logpass = request.json['password']
    gethpass = logpass + 'xaaa'

    user = User(did, email, logpass, gethpass)

    # add user to db
    result = api_page.resource['mongo'].add_user(user)
    response = json.dumps(result, default=json_util.default)
    return response


@api_page.route('/signin', methods=['POST'])
def login():
    login_did = request.json['did']
    # login_pwd = bcrypt.hashpw(request.json['password'].encode('UTF-8'), bcrypt.gensalt())
    login_pwd = request.json['password'].encode('UTF-8')
    login_pass = login_pwd.decode('ascii')

    # get a hash pwd from the given pwd
    # hashed_pwd = bcrypt.hashpw(login_pwd, bcrypt.gensalt())

    # compare it with DB
    result = api_page.resource['mongo'].auth_user_by_did(login_did, login_pass)
    print(result)
    if result['code'] == 200:
        # # Login Success
        # payload = {
        #     'email': login_email,
        #     'exp': datetime.utcnow() + timedelta(seconds=60 * 60)
        # }
        # token = jwt.encode(payload, api_page.resource['JWT_SECRET_KEY'], 'HS256')
        return jsonify({
            'code': 200,
            # 'access_token': token.decode('UTF-8')
        })
    else:
        # Login Fail
        return jsonify({
            'code': 404
        })


@api_page.route('/add_user', methods=['GET'])
def add_user():
    given_name = request.args.get('name')
    age = request.args.get('age')
    user = {'name':given_name, 'age':age}
    api_page.resource['mongo'].add_user(user)
    return 'Write Success'


@api_page.route('/del_user', methods=['GET'])
def del_user():
    given_name = request.args.get('name')
    user = {'name':given_name}
    api_page.resource['mongo'].del_user(user)
    return 'Del Success'


@api_page.route('/find_user', methods=['GET'])
def find_user():
    given_name = request.args.get('name')
    user = {'name':given_name}
    user = api_page.resource['mongo'].find_user(user)
    return user


@api_page.route('/update_user', methods=['GET'])
def update_user():
    given_name = request.args.get('name')
    user = {'name':given_name}
    user = api_page.resource['mongo'].update_user(user)
    return user
