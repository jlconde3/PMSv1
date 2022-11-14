from flask import render_template, Blueprint, request,g, make_response, redirect, url_for, flash
from common import MySQLHelper, InputClass
from auth import login_required, CustomViews
from datetime import datetime


bp = Blueprint('actions', __name__, url_prefix='/actions')

bp.add_url_rule('/create_action', view_func=CustomViews.as_view('/create_action','/tools/actions/create_action.html'))
bp.add_url_rule('/modify_action', view_func=CustomViews.as_view('/modify_action','/tools/actions/modify_action.html'))

def generate_action_code (MySQL) -> str:
    MySQL.cursor.execute('SELECT action_code FROM actions ORDER BY id DESC LIMIT 1')
    action_code = MySQL.cursor.fetchone()

    if action_code is None:
        action_code = 'ACT1000001'
    else:
        action_code = action_code[0][:3]+ str(int(action_code[0][3:])+1)




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

    project = InputClass(request.form['project_code'].upper().strip())
    customer = InputClass(request.form['customer_code'].upper().strip())
    type = InputClass(request.form['action_type'].upper().strip())
    date =InputClass(request.form['action_date'].upper().strip())
    discipline = InputClass(request.form['discipline_code'].upper().strip())
    phase = InputClass(request.form['phase_code'].upper().strip())
    description = InputClass(request.form['action_description'].upper().strip())
    codes = request.form.getlist('custom_code')
    zones = request.form.getlist('subaction_zone')
    areas = request.form.getlist('subaction_area')
    times = request.form.getlist('subaction_time')

    MySQL = MySQLHelper()

    if project.check_input_project(MySQL):
        check_all = True
    else:
        check_all = False

    if check_all and discipline.check_input_value(MySQL=MySQL,field='discipline',table='tasks',project=project.value):
        check_all = True
    else:
        check_all = False
    
    if check_all and phase.check_input_value(MySQL=MySQL,field='phase',table='areas',project=project.value):
        check_all = True
    else:
        check_all = False

    if check_all and customer.check_for_sensitive_chars():
        check_all = True
    else:
        check_all = False

    if check_all and type.check_input_value(MySQL=MySQL,field='station',table='tasks',project=project.value):
        check_all = True
    else:
        check_all = False

    date.check_for_date()

    if check_all and description.check_for_sensitive_chars():
        check_all = True
    else:
        check_all = False

    for i in codes:
        value = InputClass(i)
        if check_all and value.check_for_sensitive_chars():
            check_all = True
        else:
            check_all = False

    for i in zones:
        value = InputClass(i)
        if check_all and value.check_input_value(MySQL=MySQL,field='zone',table='areas',project=project.value):
            check_all = True
        else:
            check_all = False

    for i in areas:
        value = InputClass(i)
        if check_all and value.check_input_value(MySQL=MySQL,field='area',table='areas',project=project.value):
            check_all = True
        else:
            check_all = False
    
    for i in times:
        value = InputClass(i)
        if check_all and value.check_for_digits():
            check_all = True
        else:
            check_all = False

    try:
        if check_all:
            action_code = generate_action_code(MySQL)

            for code,zone,area,time in zip(codes,zones,areas, times):

                print([action_code,project.value,customer.value,type.value,date.value,discipline.value,phase.value,description.value,generate_subaction_code(MySQL),code,zone,area,time, g.user, datetime.today(),'Not assigned'])

                MySQL.cursor.execute(
                    """
                    INSERT INTO actions (action_code,project,customer_code,type,date_recived,
                    discipline,phase,description,subaction_code,custom_code,zone,area,time,
                    user,date, status)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (action_code,project.value,customer.value,type.value,date.value,discipline.value,phase.value,description.value,
                    generate_subaction_code(MySQL),code,zone,area,time, g.user, datetime.today(),'Not assigned'))

                MySQL.con.commit()

            MySQL.con.close()

            return make_response('Success',201)

        return make_response('Some values are not correct',401)

    except MySQL.Error as e:
        print(e)
        MySQL.con.close()
        return make_response("Not saved",401)



