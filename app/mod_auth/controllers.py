# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for,jsonify

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import module forms
#from app.mod_auth.forms import LoginForm

# Import module models (i.e. User)
from app.mod_auth.models import *

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    return jsonify(get_desa(1101010003))

@mod_auth.route('/insert/', methods=['GET', 'POST'])
def insert():
    return insert_tiket()

@mod_auth.route('/post/', methods=['GET', 'POST'])
def post():
    data = {'pertama': 'pertama text','kedua':'kedua text'}
    return postx(**data)