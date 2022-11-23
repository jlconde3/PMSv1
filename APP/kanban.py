import json

from flask import render_template, Blueprint, request, make_response
from auth import login_required
from common import MySQLHelper, InputClass


bp = Blueprint('kanban', __name__, url_prefix='/kanban')

@bp.route('/', methods=['GET'])
@login_required
def main():
    return render_template('/tools/kanban/home.html')


@bp.route('/retrive_cards', methods=['POST'])
@login_required
def retrive_cards():
    data = request.get_json()

    project = InputClass(data['project'])
    field = InputClass(data['field'])
    value = InputClass(data['value'])


    if field.value.lower() in {'discipline','system','phase','zone','area'}:
        table = 'areas'
    elif field.value.lower() in {'line','station'}:
        table = 'tasks'
    else:
        return make_response(f'Value {field.value} not found',401)

    MySQL = MySQLHelper()

    if not project.check_input_project(MySQL=MySQL):
        MySQL.con.close()
        return make_response(f'Project {project.value} not found',401)

    if not value.check_input_value(MySQL=MySQL,field=field.value.lower(),table=table,project=project.value):
        MySQL.con.close()
        return make_response(f'Value {value.value} not found',403)
    

    MySQL.cursor.execute(f"SELECT status,code,has_message,description,users FROM wp WHERE project = '{project.value}' AND {field.value.lower()} = '{value.value}'")
    query = MySQL.cursor.fetchall()
    MySQL.con.close()
    query_list = []
    for i in query:
        query_list.append(list(i))
    
    for i in query_list:
        i[4] = i[4].split(',')
    
    return json.dumps(query_list)
