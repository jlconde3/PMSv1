
from flask import Blueprint

bp = Blueprint('tools', __name__, url_prefix='/tools',static_folder='static', template_folder='templates')
