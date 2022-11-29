from flask import render_template, Blueprint, request,g, make_response
from common import MySQLHelper,InputClass
from auth import login_required, CustomViews

bp = Blueprint('wps', __name__, url_prefix='/wps')

bp.add_url_rule('/create_wp', view_func=CustomViews.as_view('/create_wp','/tools/wps/create_wp.html'))
bp.add_url_rule('/modify_wp', view_func=CustomViews.as_view('/modify_wp','/tools/wps/modify_wp.html'))

@bp.route('/info')
@login_required
def info ():
    wp = request.args.get('wp')

    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT * FROM wp WHERE code = %s',(wp,))
    response = MySQL.cursor.fetchone()
    print (response)

    return render_template('/tools/wps/info_wp.html', 
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
        volumn_value = response[16],
        complexity_value = response[17],
        contracted_time_value = response[18],
        planned_time_value = response[19],
        scheduled_time_value = response[20],
        remark = response[22],
        custom_code = response[25]
    )

def split_data (data:str):
    if data is None:
        return []
    return data.split(",")