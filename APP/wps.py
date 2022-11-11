from flask import render_template, Blueprint, request,g, make_response
from auth import login_required, CustomViews
from common import MySQLHelper, InputClass

bp = Blueprint('wps', __name__, url_prefix='/wps')

bp.add_url_rule('/create_wp', view_func=CustomViews.as_view('/create_wp','/tools/wps/create_wp.html'))
bp.add_url_rule('/modify_wp', view_func=CustomViews.as_view('/modify_wp','/tools/wps/modify_wp.html'))