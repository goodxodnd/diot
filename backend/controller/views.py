from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

view_page = Blueprint('view_page', 'view_page', template_folder='templates')
view_page.resource = {}


@view_page.route('/', methods=['GET'])
def get_main():
    try:
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
