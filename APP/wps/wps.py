
from general.general import MySQLHelper, InputClass
from auth.auth import login_required, CustomViews

from flask import render_template, Blueprint, request,g, make_response
from datetime import datetime

bp = Blueprint('wps', __name__, url_prefix='/wps', template_folder='templates')

bp.add_url_rule('/create', view_func=CustomViews.as_view('/create','wps/create.html'))
bp.add_url_rule('/modify', view_func=CustomViews.as_view('/modify','wps/modify.html'))

@bp.route('/info')
@login_required
def info ():
    
    project = InputClass(request.args.get('project')) 
    wp = InputClass(request.args.get('wp'))

    MySQL = MySQLHelper()

    if not project.check_input_project(MySQL=MySQL):
        MySQL.con.close()
        return make_response(f'Project {project.value} not found',401)

    if not wp.check_input_value(MySQL=MySQL,field='code',table='wp', project=project.value):
        MySQL.con.close()
        return make_response(f'Value {wp.value} not found',401)

    MySQL.cursor.execute('SELECT * FROM wp WHERE project = %s AND code = %s',(project.value,wp.value))
    response = MySQL.cursor.fetchone()
    MySQL.con.close()


    return render_template('wps/info.html', 
        wp_code = response[1],
        date_1 = response[3],
        date_2 = response[4],
        project = response[5],
        discipline = response[6],
        phase = response[7],
        system = response[8],
        line = response[9],
        station = response[10],
        zone = response[11],
        actions = split_data(response[12]),
        areas = split_data(response[13]),
        tasks = split_data(response[14]),
        dif_value = response[15],
        volume_value = response[16],
        complexity_value = response[17],
        contracted_time_value = response[18],
        planned_time_value = response[19],
        scheduled_time_value = response[20],
        status = response[21],
        remark = response[22],
        custom_code = response[25]
    )

def split_data (data:str):
    if data is None:
        return []
    return data.split(",")


@bp.route('/info_save', methods=['POST'])
@login_required
def info_save():

    project = InputClass(request.args.get('project')) 
    wp = InputClass(request.args.get('wp')) 
    status = InputClass(request.form['status'])
    remark = InputClass(request.form['remark'])

    if not project.check_input_project():
        return make_response(f'Project {project.value} not found',401)
        
    if not status.value in  ['TO DO','IN PROGRESS','ON HOLD','DONE','CANCEL']:
        return make_response(f'Value {status.value} not found',401)
    
    if not remark.check_for_sensitive_chars():
        return make_response(f'Value {remark.value} has special chars not allowed',401)

    MySQL = MySQLHelper()

    if not wp.check_input_value(MySQL=MySQL,field='code',table='wp', project=project.value):
        MySQL.con.close()
        return make_response(f'Value {wp.value} not found',401)
    


    MySQL.cursor.execute('SELECT * FROM wp WHERE project = %s AND code = %s',(project.value,wp.value))
    response = MySQL.cursor.fetchone()
    MySQL.con.close()

    return "Hola"



    