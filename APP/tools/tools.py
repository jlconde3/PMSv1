
from general.general import InputClass
from auth.auth import CustomViews

from flask import Blueprint

bp = Blueprint('tools', __name__, url_prefix='/tools',static_folder='static', template_folder='templates')


bp.add_url_rule('/', view_func=CustomViews.as_view('/','tools/tools.html'))