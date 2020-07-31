from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from bson import json_util
import json
from backend.models.dom import Config
from backend.controller.config import CONFIG, Mode, ResCode
from backend.controller.core import EthCore2
from backend.controller import core
from backend.controller.core import OwnershipManager

view_page = Blueprint('view_page', 'view_page', template_folder='templates')
view_page.resource = {}


@view_page.route('/', methods=['GET'])
def get_main():
    try:

        system_dapp_addr_result = view_page.resource['mongo'].systemdapp_is_exist()

        if system_dapp_addr_result == True:
            system_dapp_read = view_page.resource['mongo'].find_systemdapp()
            print(system_dapp_read)
            params = system_dapp_read['payload']
            system_dapp_addr = params['system_dapp_addr']
            print('a', system_dapp_addr)

            view_page.resource['ownership_manager'].set_system_dapp(system_dapp_addr)

            return render_template('index.html')

        else:
            print('system deploy.')
            ret = view_page.resource['ownership_manager'].deploy_system_dapp(CONFIG['SYSTEM_EOA'], CONFIG['SYSTEM_GETHPASS'])
            if ret['code'] == ResCode.OK.value:
                system_dapp_addr = ret['deployResult']['contractAddress']
                print(system_dapp_addr)
                view_page.resource['ownership_manager'].set_system_dapp(system_dapp_addr)

                info = 1
                payload = Config(info, system_dapp_addr)

                mongoResult = view_page.resource['mongo'].add_systemdapp(payload)
                response = json.dumps(mongoResult, default=json_util.default)
            return render_template('index.html')

    except TemplateNotFound:
        abort(404)


@view_page.route('/dashboard', methods=['GET'])
def get_dashboard():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/signin', methods=['GET'])
def get_signin():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/signup', methods=['GET'])
def get_signup():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/alarm', methods=['GET'])
def get_alarm():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/authorityaccept', methods=['GET'])
def get_authorityaccept():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/authorityrequest', methods=['GET'])
def get_authorityrequest():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/devicelist', methods=['GET'])
def get_devicelist():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/devicesearch', methods=['GET'])
def get_devicesearch():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/main', methods=['GET'])
def get_mainpage():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/mypage', methods=['GET'])
def get_mypage():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/ownershipaccept', methods=['GET'])
def get_ownershipaccept():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/ownershiprequest', methods=['GET'])
def get_ownershiprequest():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/service', methods=['GET'])
def get_service():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/serviceregister', methods=['GET'])
def get_serviceregister():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/tieraccept', methods=['GET'])
def get_tieraccept():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/tiermanagement', methods=['GET'])
def get_tiermanagement():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/tierrequest', methods=['GET'])
def get_tierrequest():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/tierserviceset', methods=['GET'])
def get_tierserviceset():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)
