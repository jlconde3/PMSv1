from crypt import methods
from flask import (render_template, Blueprint)
from auth import login_required


bp = Blueprint('data', __name__, url_prefix='/data')

@bp.route('/', methods=['GET'])
@login_required
def main():
    return render_template('data.html')