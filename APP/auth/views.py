from auth.auth import login_model, logout_model

import functools
from flask import request, render_template, Blueprint, redirect, url_for, session, g

bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates', static_folder='statics')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user_id is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


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




