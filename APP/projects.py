from flask import render_template, Blueprint, request,g, make_response
from common import MySQLHelper,InputClass
from auth import login_required, CustomViews

bp = Blueprint('projects', __name__, url_prefix='/projects')

bp.add_url_rule('/create_project', view_func=CustomViews.as_view('/create_proejct','/tools/projects/create_project.html'))
bp.add_url_rule('/modify_project', view_func=CustomViews.as_view('/modify_project','/tools/projects/modify_project.html'))

@bp.route('/create', methods=['POST'])
@login_required
def create ():
    code = InputClass(request.form['code'])
    name = InputClass(request.form['name'])
    client = InputClass(request.form['client'])
    section = InputClass(request.form['section'])
    division = InputClass(request.form['division'])
    budget = InputClass(request.form['budget'])
    margin = InputClass(request.form['margin'])
    default = InputClass(request.form['default'])
    action = InputClass(request.form['action'])
    management = InputClass(request.form['management'])
    others = InputClass(request.form['others'])
    
    for i in [code,name,client,section, division, budget,margin, default,action, management, others]:
        print(i)
    return "Hola"

