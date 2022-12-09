import functools

from general.general import InputClass
from auth.data import *
from hashlib import sha256
from flask.views import View
from flask import render_template, Blueprint, redirect, url_for, request, session, g


bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates', static_folder='static')

def check_password_hash (user_password:str,input_password:str):
    if user_password == sha256(input_password.encode()).hexdigest():
        return True
    else:
        return False

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login_user'))
        return view(**kwargs)
    return wrapped_view

class CustomViews (View):
    methods = ["GET"]
    decorators = [login_required]

    def __init__(self,model) -> None:
        self.model = model
        self.template = model

    def dispatch_request(self):
        if request.method == "GET":
            return render_template(self.template)


def login_model (username, password):

    """
    Check if login info is correct or not. 

    :param username: username from form.
    :param password: password from form.
    Return True if login is correct and False if not with an error information.
    """

    username = InputClass(username)

    error = None

    if not username.check_for_sensitive_chars():
        error = 'Special chars not allowed in username field'

    user = login_data(username.value)

    if user is None:
        error = 'Incorrect username'
    elif not check_password_hash(user[1], password):
        error = 'Incorrect password'
        return [False,error, username.value]

    if error is None:
        client = login_client(user[0])
        session.clear()
        session['user_id'] = user[0]
        session['user_client'] = client[0]
        return [True]
    
    return[False,error,None]


def logout_model():
    session['user_id'] = None
    session['user_rol'] = None



