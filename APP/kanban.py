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
    value = InputClass(data['value'])


    MySQL = MySQLHelper()
    if not project.check_input_project(MySQL=MySQL):
        MySQL.con.close()
        return make_response(f'Project {project.value} not found',401)
    
    if not value.check_input_value(MySQL=MySQL,field='station',table='tasks',project=project.value):
        MySQL.con.close()
        return make_response(f'Value {value.value} not found',403)


    MySQL.cursor.execute('SELECT status,code,description,users FROM wp WHERE project = %s AND station=%s',(project.value,value.value))
    query = MySQL.cursor.fetchall()
    for i in query:
        print(i)
        
    MySQL.con.close()

    return json.dumps(query)