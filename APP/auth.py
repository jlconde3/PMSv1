import functools

from flask import (render_template, Blueprint, redirect, url_for, request, session, g)
from hashlib import sha256
from common import MySQLHelper, InputClass
from flask import render_template, request
from flask.views import View


bp = Blueprint('auth', __name__, url_prefix='/auth')

def check_password_hash (user_password:str,input_password:str):
    if user_password == sha256(input_password.encode()).hexdigest():
        return True
    else:
        return False

@bp.route('/login', methods=('GET', 'POST'))
def login_user ():
    if request.method == 'POST':

        username = InputClass(request.form['username'])
        password = InputClass(request.form['password'])

        if username.check_for_sensitive_chars() and password.check_for_sensitive_chars():
            error = None

            MySQL = MySQLHelper()
            MySQL.cursor.execute('SELECT * FROM users WHERE user = %s ORDER BY id DESC LIMIT 1', (username.format_upper_case(),))
            user = MySQL.cursor.fetchone()
            MySQL.con.close()

            if user is None:
                error = 'Incorrect username'
            elif not check_password_hash(user[5], password.value):
                error = 'Incorrect password'

            if error is None:
                session.clear()
                session['user_id'] = user[1]
                return redirect(url_for('tools./'))
            else:
                return error
        
        else: 
            error = 'You introduce special characters not allowed'
            return error
        
    return render_template('public/login.html')

@bp.route('/logout', methods=('GET', 'POST'))
def logout ():
    session.clear()
    return redirect(url_for('auth.login_user'))

@bp.before_app_request
def load_logged_user ():
    user_id = session.get('user_id')
    if  user_id is None:
        g.user = None
    else: 
        g.user = user_id

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

    def __init__(self,module,model) -> None:
        self.model = model
        self.template = f'/{module}/{model}.html'

    def dispatch_request(self):
        if request.method == "GET":
            return render_template(self.template)