from flask import (render_template, Blueprint)
from auth import login_required
from common import MySQLHelper


bp = Blueprint('kanban', __name__, url_prefix='/kanban')

@bp.route('/', methods=['GET'])
@login_required
def main():
    return render_template('/tools/kanban/home.html')