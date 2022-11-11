from flask import render_template, Blueprint, request,g, make_response
from common import MySQLHelper, InputClass
from auth import login_required, CustomViews
from datetime import datetime

bp = Blueprint('actions', __name__, url_prefix='/actions')

bp.add_url_rule('/create_action', view_func=CustomViews.as_view('/create_action','/tools/actions/create_action.html'))
bp.add_url_rule('/modify_action', view_func=CustomViews.as_view('/modify_action','/tools/actions/modify_action.html'))



def generate_action_subaction_code (MySQL) -> str:
    
    MySQL.cursor.execute('SELECT action_code FROM actions ORDER BY id DESC LIMIT 1')
    action_code = MySQL.cursor.fetchone()
    if action_code is None:
        action_code = 'ACT1000001'
    else:
        action_code = action_code[0][:3]+ str(int(action_code[0][3:])+1)

    MySQL.cursor.execute('SELECT subaction_code FROM actions ORDER BY id DESC LIMIT 1')
    subaction_code = MySQL.cursor.fetchone()
    MySQL.con.close()
    if subaction_code is None:
       subaction_code = 'SUBACT10000001'
    else:
        subaction_code = subaction_code[0][:6]+ str(int(subaction_code[0][6:])+1)

    return [action_code,subaction_code]



@bp.route('/create', methods=['POST'])
@login_required
def create_action():
    data = request.is_json
    print(data)
    """
    project = InputClass(data['project_code'])
    customer= InputClass(data['customer_code'])
    type = InputClass(data['action_type'])
    date = InputClass(data['action_date'])
    discipline = InputClass(data['discipline_code'])
    phase = InputClass(data['phase_code'])
    description = InputClass(data['action_description'])
    codes = InputClass(data['custom_code'])
    zones = InputClass(data['subaction_zone'])
    areas = InputClass(data['subaction_area'])
    times = InputClass(data['subaction_time'])

    for i in [project, customer, type, date, discipline, phase, description]:
        print(i.check_for_sensitive_chars())
        if not i.check_for_sensitive_chars():
            check_all = False
            break

    if check_all:
        MySQL = MySQLHelper()
        code = generate_action_subaction_code(MySQL)

        for code,zone,area,time in zip():
            MySQL.cursor.execute('INSERT INTO actions (action_code,project,customer_code,type,date_recived,discipline,phase,description,subaction_code,custom_code,zone,area,time,user,date)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')

    """

    return data
