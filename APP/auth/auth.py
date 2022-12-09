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
        if g.user_id is None:
            return redirect(url_for('auth.login'))
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



@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        login_status = login_model(request.form['username'],request.form['password'])

        if login_status[0]:
            return redirect(url_for('index'))
        return render_template('auth/login.html', error = login_status[1], user = login_status[2])

    elif request.method == 'GET':
        return render_template('auth/login.html')


@bp.route('/logout', methods=('GET', 'POST'))
def logout():
    logout_model()
    return redirect(url_for('auth.login'))


@bp.before_app_request
def load_logged_user ():
    user_id = session.get('user_id')
    user_rol = session.get('user_rol')
    if  user_id is None:
        g.user_id = None
        g.user_rol = None
    else: 
        g.user_id = user_id
        g.user_rol = user_rol



