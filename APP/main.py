from flask import (render_template, Blueprint)

from auth import login_required


bp = Blueprint("main", __name__, url_prefix="/main")

@bp.route('/', methods=('GET', 'POST'))
@login_required
def main ():
    return render_template ("main.html")