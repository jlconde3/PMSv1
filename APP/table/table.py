
from general.general import MySQLHelper, InputClass
from auth.auth import login_required, CustomViews

from flask import render_template, Blueprint

bp = Blueprint('data', __name__, url_prefix='/data', static_folder='static', template_folder='templates')
bp.add_url_rule('/', view_func=CustomViews.as_view('/','table/base.html'))



