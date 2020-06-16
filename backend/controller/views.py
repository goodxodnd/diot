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