
from general.general import MySQLHelper, InputClass
from auth.auth import login_required, CustomViews

from flask import render_template, Blueprint

bp = Blueprint('data', __name__, url_prefix='/data', static_folder='static', template_folder='temaplates')

@bp.route('/', methods=['GET'])
@login_required
def main():
    return render_template('/data/home.html')

