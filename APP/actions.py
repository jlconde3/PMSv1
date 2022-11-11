from flask import render_template, Blueprint, request,g, make_response
from auth import login_required, CustomViews
from common import MySQLHelper, InputClass

bp = Blueprint('actions', __name__, url_prefix='/actions')

bp.add_url_rule('/create_action', view_func=CustomViews.as_view('/create_action','/tools/actions/create_action.html'))
bp.add_url_rule('/modify_action', view_func=CustomViews.as_view('/modify_action','/tools/actions/modify_action.html'))