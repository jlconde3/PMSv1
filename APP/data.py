from flask import (render_template, Blueprint)
from auth import login_required
from common import MySQL


bp = Blueprint('data', __name__, url_prefix='/data')

@bp.route('/', methods=['GET'])
@login_required
def main():
    return render_template('/data/home.html')


@bp.route('/wp', methods=['GET'])
@login_required
def wp():
    MySQL.cursor.execute('SELECT project,code, status,scheduled_time FROM wp')
    data = MySQL.cursor.fetchall()
    return data