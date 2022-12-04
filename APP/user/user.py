from flask import render_template, Blueprint, request
from auth import login_required, CustomViews


bp = Blueprint('user', __name__, url_prefix='/user')


bp.add_url_rule('/', view_func=CustomViews.as_view('/', '/public/profile.html'))
bp.add_url_rule('/settings', view_func=CustomViews.as_view('/settings','/public/settings.html'))



