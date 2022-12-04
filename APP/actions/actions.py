import json

from flask import render_template, Blueprint, request,g, make_response, redirect, url_for, flash
from common import MySQLHelper, InputClass, format_mysql_list
from APP.auth import login_required, CustomViews
from datetime import datetime
from decimal import Decimal


bp = Blueprint('actions', __name__, url_prefix='/actions', template_folder='template', static_folder='static')

bp.add_url_rule('/create_action', view_func=CustomViews.as_view('/create_action','/tools/actions/create_action.html'))
bp.add_url_rule('/modify_action', view_func=CustomViews.as_view('/modify_action','/tools/actions/modify_action.html'))
bp.add_url_rule('/modify_subaction', view_func=CustomViews.as_view('/modify_subaction','/tools/actions/modify_subaction.html'))

def generate_action_code (MySQL) -> str:
    MySQL.cursor.execute('SELECT action_code FROM actions ORDER BY id DESC LIMIT 1')
    action_code = MySQL.cursor.fetchone()

    if action_code is None:
        action_code = 'ACT1000001'
    else:
        action_code = action_code[0][:3]+ str(int(action_code[0][3:])+1)
    return action_code

def generate_subaction_code(MySQL) -> str:
    MySQL.cursor.execute('SELECT subaction_code FROM actions ORDER BY id DESC LIMIT 1')
    subaction_code = MySQL.cursor.fetchone()

    if subaction_code is None:
       subaction_code = 'SUBACT10000001'
    else:
        subaction_code = subaction_code[0][:6]+ str(int(subaction_code[0][6:])+1)

    return subaction_code


@bp.route('/create', methods=['POST'])
@login_required
def create_action():

    project = InputClass(request.form['project'])
    phase = InputClass(request.form['phase'])
    customer = InputClass(request.form['customer'])

    date =InputClass(request.form['date'])

    discipline = InputClass(request.form['discipline'])
    system = InputClass(request.form['system'])
    type = InputClass(request.form['type'])
    description = InputClass(request.form['description'])

    codes = request.form.getlist('custom')
    zones = request.form.getlist('subaction_zone')
    areas = request.form.getlist('subaction_area')
    times = request.form.getlist('subaction_time')

    error = None
    MySQL = MySQLHelper()

    if not project.check_input_project(MySQL=MySQL):
        error = make_response(f'Project {project.value} not found',401)

    if error is None:
        for i,field,table in zip(
            [phase,discipline,system,type],
            ['phase','discipline','system1','station'],
            ['areas','areas','areas','tasks']):
            if not i.check_input_value(MySQL=MySQL,field=field,table=table,project=project.value):
                error = make_response(f'Value {i.value} not found',401)
                break

    if error is None:
        for i in [customer,description]:
            if not i.check_for_sensitive_chars():
                error = make_response(f'Value {i.value} has special chars not allowed',401)
                break

    if error is None:
        for i in codes:
            i = InputClass(i)
            if not i.check_for_sensitive_chars():
                error = make_response(f'Value {i.value} has special chars not allowed',401)
                break

    if error is None:
        for i in zones:
            i = InputClass(i)
            if not i.check_input_value(MySQL=MySQL,field='zone',table='areas',project=project.value):
                error = make_response(f'Value {i.value} not found',401)
                break

    if error is None:
        for i in areas:
            i = InputClass(i)
            if not i.check_input_value(MySQL=MySQL,field='area',table='areas',project=project.value):
                error = make_response(f'Value {i.value} not found',401)
                break
            
    if error is None:
        for i in times:
            i = InputClass(i)
            if not i.check_for_digits():
                error = make_response(f'Incorrect format:{i.value}',401)
                break

    if error is None:
        date.check_for_date()

    if error is None:
        action_code = generate_action_code(MySQL)
        
        for code,zone,area,time in zip(codes,zones,areas, times):
            MySQL.cursor.execute(
                """
                INSERT INTO actions (action_code,project,customer_code,type,date_recived,
                discipline,phase,description,subaction_code,custom_code,zone,area,time,
                user,date,system1,status)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                (action_code,project.value,customer.value,type.value,date.value,discipline.value,phase.value,description.value,
                generate_subaction_code(MySQL),code,zone,area,time, g.user, datetime.today(),system.value,'Not assigned'))
            MySQL.con.commit()
            
        MySQL.con.close()
        return make_response('Success',201)
    
    MySQL.con.close()
    return error

@bp.route('/retrive_action', methods=['POST'])
@login_required
def retrive_action():
    data = request.get_json()
    project = InputClass(data['project'])
    action = InputClass(data['action'])

    MySQL = MySQLHelper()
    
    if not project.check_input_project(MySQL=MySQL):
        MySQL.con.close()
        return make_response(f'Project {project.value} not found',401)

    if not action.check_for_sensitive_chars():
        MySQL.con.close()
        return make_response(f'Value {action.value} has special chars not allowed',402)
    
    MySQL = MySQLHelper()

    if not action.check_input_value(MySQL=MySQL,field='action_code',table='actions',project=project.value):
        MySQL.con.close()
        return make_response(f'Value {action.value} not found',403)
    
    MySQL.cursor.execute("SELECT customer_code,type,discipline,phase,description,system1,date_recived FROM actions WHERE project=%s AND action_code=%s ORDER BY date DESC LIMIT 1",(project.value,action.value))
    db_response = MySQL.cursor.fetchone()

    print(db_response)
    MySQL.con.close()

    row_data = []
    for value in db_response:
        if type(value) is Decimal:
            row_data.append(float(value))
        else:
            row_data.append(str(value))

    return json.dumps({'response':row_data})


@bp.route('/retrive_subaction', methods=['POST'])
@login_required
def retrive_subaction():
    data = request.get_json()
    project = InputClass(data['project'])
    subaction = InputClass(data['subaction'])

    MySQL = MySQLHelper()
    
    if not project.check_input_project(MySQL=MySQL):
        MySQL.con.close()
        return make_response(f'Project {project.value} not found',401)

    if not subaction.check_for_sensitive_chars():
        MySQL.con.close()
        return make_response(f'Value {subaction.value} has special chars not allowed',402)
    
    MySQL = MySQLHelper()

    if not subaction.check_input_value(MySQL=MySQL,field='subaction_code',table='actions',project=project.value):
        MySQL.con.close()
        return make_response(f'Value {subaction.value} not found',403)
    
    MySQL.cursor.execute("SELECT action_code,customer_code,custom_code,zone,area,time,status FROM actions WHERE project=%s AND subaction_code=%s ORDER BY date DESC LIMIT 1",(project.value,subaction.value))
    response = MySQL.cursor.fetchone()

    MySQL.con.close()

    row_data = []
    for value in response:
        if type(value) is Decimal:
            row_data.append(float(value))
        else:
            row_data.append(str(value))

    return json.dumps({'response':row_data})

@bp.route('/modify_action', methods=['POST'])
@login_required
def modify_action ():
    project = InputClass(request.form['project'])
    action = InputClass(request.form['action'])
    client = InputClass(request.form['client'])
    description = InputClass(request.form['description'])

    MySQL = MySQLHelper()

    if not project.check_input_project(MySQL=MySQL):
        MySQL.con.close()
        return make_response(f'Project {project.value} not found',401)
    
    for i in [client,client,description]:
        if not i.check_for_sensitive_chars():
            MySQL.con.close()
            return make_response(f'Value {i.value} has special chars not allowed',402)


    if not action.check_input_value(MySQL=MySQL,field='action_code',table='actions',project=project.value):
        MySQL.con.close()
        return make_response(f'Value {action.value} not found',403)

    MySQL.cursor.execute("SELECT DISTINCT subaction_code FROM actions WHERE project=%s AND action_code=%s",(project.value,action.value))
    subactions = format_mysql_list( MySQL.cursor.fetchall())

    MySQL.cursor.execute("SELECT type,date_recived,discipline,phase,system FROM actions WHERE project=%s AND action_code=%s ORDER BY date DESC LIMIT 1",(project.value,action.value))
    actions = format_mysql_list( MySQL.cursor.fetchone())

    for i in subactions:
        MySQL.cursor.execute("SELECT custom_code,zone,area,time,status FROM actions WHERE project=%s AND subaction_code=%s ORDER BY date DESC LIMIT 1",(project.value,i))
        subaction_values = MySQL.cursor.fetchone()
        MySQL.cursor.execute(
            """
            INSERT INTO actions (action_code,project,customer_code,type,date_recived,
            discipline,phase,description,subaction_code,custom_code,zone,area,time,
            user,date,system1,status)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (action.value,project.value,client.value,actions[0],actions[1],actions[2],actions[3],description.value,
            i,subaction_values[0],subaction_values[1],subaction_values[2],subaction_values[3], g.user, datetime.today(),actions[4],subaction_values[4]))
        MySQL.con.commit()

    MySQL.con.close()
    return "Success"


@bp.route('/modify_subaction', methods=['POST'])
@login_required
def modify_subaction ():
    
    project = InputClass(request.form['project'])
    subaction = InputClass(request.form['subaction'])
    action = InputClass(request.form['action'])
    client = InputClass(request.form['client'])
    custom = InputClass(request.form['custom'])
    zone = InputClass(request.form['zone'])
    area = InputClass(request.form['area'])
    time = InputClass(request.form['time'])
    status = InputClass(request.form['status'])

    MySQL = MySQLHelper()

    if not project.check_input_project(MySQL=MySQL):
        MySQL.con.close()
        return make_response(f'Project {project.value} not found',401)
    
    for i in [client,custom,status]:
        if not i.check_for_sensitive_chars():
            MySQL.con.close()
            return make_response(f'Value {i.value} has special chars not allowed',402)


    for i,field,table in zip([action,subaction,zone,area],
    ['action_code','subaction_code','zone','area','station'],
    ['actions','actions','areas','areas','tasks']):
        if not i.check_input_value(MySQL=MySQL,field=field,table=table,project=project.value):
            MySQL.con.close()
            return make_response(f'Value {i.value} not found',403)

    if not time.check_for_digits():
        MySQL.con.close()
        return make_response(f'Time {i.value} has not the correct format',404)



    MySQL.cursor.execute("""SELECT type,date_recived,discipline,phase,description,system1
    FROM actions WHERE project=%s AND action_code=%s ORDER BY date DESC LIMIT 1""",(project.value,action.value))
    response = MySQL.cursor.fetchone()

    MySQL.cursor.execute(
        """
        INSERT INTO actions (action_code,project,customer_code,type,date_recived,
        discipline,phase,description,subaction_code,custom_code,zone,area,time,
        user,date,system1,status)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
        (action.value,project.value,client.value,response[0],response[1],response[2],response[3],
        response[4],subaction.value,custom.value,zone.value,area.value,time.value,g.user,
        datetime.today(),response[5],status.value))
    MySQL.con.commit()
    MySQL.con.close()

    return make_response('Success',201)
    
