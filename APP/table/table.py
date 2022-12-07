
from general.general import MySQLHelper, InputClass
from auth.auth import login_required, CustomViews

from flask import render_template, Blueprint

bp = Blueprint('table', __name__, url_prefix='/table', static_folder='static', template_folder='templates')
bp.add_url_rule('/', view_func=CustomViews.as_view('/','table/base.html'))



