from flask import render_template, Blueprint, request
from auth.auth import login_required, CustomViews


bp = Blueprint('user', __name__, url_prefix='/user', template_folder='templates')


bp.add_url_rule('/', view_func=CustomViews.as_view('/', 'user/profile.html'))




