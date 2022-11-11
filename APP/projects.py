from flask import render_template, Blueprint, request,g, make_response
from common import MySQLHelper,InputClass
from auth import login_required, CustomViews

bp = Blueprint('projects', __name__, url_prefix='/projects')

bp.add_url_rule('/create_project', view_func=CustomViews.as_view('/create_proejct','/tools/projects/create_project.html'))
bp.add_url_rule('/modify_project', view_func=CustomViews.as_view('/modify_project','/tools/projects/modify_project.html'))