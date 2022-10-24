from flask import (render_template, Blueprint)
from auth import login_required


bp = Blueprint('wp', __name__, url_prefix='/wp')