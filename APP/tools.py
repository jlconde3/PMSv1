import json

from common import MySQL, format_upper_case, format_dots, remove_spaces, format_mysql_list, format_actions_list
from flask import render_template, Blueprint, request,g, Response
from auth import login_required
from flask.views import View
from datetime import datetime

bp = Blueprint('tools', __name__, url_prefix='/tools')

class Tools(View):
    methods = ["GET"]
    decorators = [login_required]

    def __init__(self,model) -> None:
        self.model = model
        self.template = f'/tools/{model}.html'

    def dispatch_request(self):
        if request.method == "GET":
            return render_template(self.template)


bp.add_url_rule('/', view_func=Tools.as_view('/', 'home'))
bp.add_url_rule('/create_project', view_func=Tools.as_view('/create_project', 'create_project'))
bp.add_url_rule('/modify_project', view_func=Tools.as_view('/modify_project', 'modify_project'))
bp.add_url_rule('/create_action', view_func=Tools.as_view('/create_action', 'create_action'))
bp.add_url_rule('/modify_action', view_func=Tools.as_view('/modify_action', 'modify_action'))
bp.add_url_rule('/create_wp', view_func=Tools.as_view('/create_wp', 'create_wp'))
bp.add_url_rule('/modify_wp', view_func=Tools.as_view('/modify_wp', 'modify_wp'))
bp.add_url_rule('/modify_workspace', view_func=Tools.as_view('/modify_worksace', 'modify_workspace'))
bp.add_url_rule('/modify_task', view_func=Tools.as_view('/modify_task', 'modify_task'))


@bp.route('/projects',methods=['GET','POST'])
def projects ():
    MySQL.cursor.execute('SELECT DISTINCT project FROM pms.areas')
    return format_mysql_list(MySQL.cursor.fetchall())

@bp.route('/disciplines',methods=['GET','POST'])
def disciplines ():
    data = request.get_json()
    MySQL.cursor.execute('SELECT DISTINCT discipline FROM pms.areas WHERE project = %s',
    (remove_spaces(format_upper_case(data['project_code'])),))
    return format_mysql_list(MySQL.cursor.fetchall())

@bp.route('/phases',methods=['GET','POST'])
def phases ():
    data = request.get_json()
    MySQL.cursor.execute('SELECT DISTINCT phase FROM pms.areas WHERE project = %s AND\
    discipline = %s',
    (remove_spaces(format_upper_case(data['project_code'])),
    remove_spaces(format_upper_case(data['discipline_code']))
    ))
    return format_mysql_list(MySQL.cursor.fetchall())

@bp.route('/types',methods=['GET','POST'])
def types ():
    data = request.get_json()
    MySQL.cursor.execute('SELECT type FROM pms.types WHERE project = %s',(remove_spaces(format_upper_case(data['project_code'])),))
    return format_mysql_list(MySQL.cursor.fetchall())

@bp.route('/zones',methods=['GET','POST'])
def zones ():
    data = request.get_json()
    MySQL.cursor.execute('SELECT DISTINCT zone FROM pms.areas WHERE project = %s AND discipline = %s AND phase = %s',
    (remove_spaces(format_upper_case(data['project_code'])),
    remove_spaces(format_upper_case(data['discipline_code'])),
    remove_spaces(format_upper_case(data['phase_code']))
    ))
    return format_mysql_list(MySQL.cursor.fetchall())

@bp.route('/areas',methods=['GET','POST'])
def areas ():
    data = request.get_json()
    MySQL.cursor.execute('SELECT DISTINCT area FROM pms.areas WHERE project = %s AND discipline = %s AND phase = %s AND zone = %s',
    (remove_spaces(format_upper_case(data['project_code'])),
    remove_spaces(format_upper_case(data['discipline_code'])),
    remove_spaces(format_upper_case(data['phase_code'])),
    remove_spaces(format_upper_case(data['zone_code']))
    ))
    return format_mysql_list(MySQL.cursor.fetchall())

@bp.route('/actions',methods=['GET','POST'])
def actions ():
    data = request.get_json()
    MySQL.cursor.execute('SELECT subaction_code, custom_code FROM pms.actions WHERE project = %s AND discipline = %s AND phase = %s AND zone = %s AND status = "Not assigned" ',
    (remove_spaces(format_upper_case(data['project_code'])),
    remove_spaces(format_upper_case(data['discipline_code'])),
    remove_spaces(format_upper_case(data['phase_code'])),
    remove_spaces(format_upper_case(data['zone_code'])) 
    ))
    return format_actions_list(MySQL.cursor.fetchall())

@bp.route('/stations',methods=['GET','POST'])
def stations ():
    data = request.get_json()
    MySQL.cursor.execute('SELECT DISTINCT station FROM pms.tasks WHERE project = %s AND discipline = %s',
    (remove_spaces(format_upper_case(data['project_code'])),
    remove_spaces(format_upper_case(data['discipline_code']))
    ))
    return format_mysql_list(MySQL.cursor.fetchall())

@bp.route('/tasks',methods=['GET','POST'])
def tasks ():
    data = request.get_json()
    MySQL.cursor.execute('SELECT DISTINCT task FROM pms.tasks WHERE project = %s AND discipline = %s AND station = %s',
    (remove_spaces(format_upper_case(data['project_code'])),
    remove_spaces(format_upper_case(data['discipline_code'])),
    remove_spaces(format_upper_case(data['station_code']))
    ))
    return format_mysql_list(MySQL.cursor.fetchall())

@bp.route('/users_projects',methods=['GET','POST'])
def users_projects():
    data = request.get_json()
    print(data)
    MySQL.cursor.execute('SELECT DISTINCT user FROM pms.users_projects WHERE project = %s',
    (remove_spaces(format_upper_case(data['project_code'])),))
    return format_mysql_list(MySQL.cursor.fetchall())


@bp.route('/create_project', methods=['POST'])
def create_project():
    data = request.get_json()

    MySQL.cursor.execute('SELECT DISTINCT code FROM pms.projects WHERE agresso_code = %s',
    (format_upper_case(remove_spaces(data['project_code'])),)) 

    if MySQL.cursor.fetchone() is not None:
        return  Response(status=412)

    try:
        MySQL.cursor.execute(
            'INSERT INTO pms.projects (agresso_code,date,name,client,section,division,budget,profit_margin,cpt_default,cpt_actions,management,extra,user)VALUES\
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (format_upper_case(remove_spaces(data['project_code'])),
            datetime.now(),
            format_upper_case(data['project_name']),
            format_upper_case(remove_spaces(data['project_client'])),
            format_upper_case(remove_spaces(data['project_section'])),
            format_upper_case(remove_spaces(data['project_division'])),
            format_dots(remove_spaces(data['project_budget'])),
            format_dots(remove_spaces(data['project_profit_margin'])),
            format_dots(remove_spaces(data['project_cpt'])),
            format_dots(remove_spaces(data['project_cpt_actions'])),
            format_dots(remove_spaces(data['project_management_cost'])),
            format_dots(remove_spaces(data['project_extra_cost'])),
            g.user))
        MySQL.con.commit()

        return Response(status=211)

    except MySQL.Error as error:
        print(error)
        return  Response(status=411)


def generate_action_code () -> str:
    MySQL.cursor.execute('SELECT action_code FROM actions ORDER BY id DESC LIMIT 1')
    code = MySQL.cursor.fetchone()
    if code is None:
        code = 'ACT1000001'
    else:
        code = code[0][:3]+ str(int(code[0][3:])+1)
    return code

def generate_subaction_code () -> str:
    MySQL.cursor.execute('SELECT subaction_code FROM actions ORDER BY id DESC LIMIT 1')
    code = MySQL.cursor.fetchone()
    if code is None:
        code = 'SUBACT10000001'
    else:
        code = code[0][:6]+ str(int(code[0][6:])+1)
    return code


@bp.route('/create_action', methods=['POST'])
def create_action():
    data = request.get_json()
    action_code = generate_action_code()

    try:
        for code,zone,area,time in zip(data['custom_code'],data['subaction_zone'],data['subaction_area'], data['subaction_time']):
            MySQL.cursor.execute(
            'INSERT INTO actions (action_code,project,\
                customer_code,type,date_recived,discipline,\
                phase,description,subaction_code,custom_code,zone,area,time,user,date)\
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (
            action_code,
            format_upper_case(remove_spaces(data['project_code'])),
            format_upper_case(remove_spaces(data['customer_code'])),
            format_upper_case(remove_spaces(data['action_type'])),
            format_upper_case(data['action_date']),
            format_upper_case(remove_spaces(data['discipline_code'])),
            format_upper_case(remove_spaces(data['phase_code'])),
            format_upper_case(remove_spaces(data['action_description'])),
            generate_subaction_code(),
            format_upper_case(remove_spaces(code)),
            format_upper_case(remove_spaces(zone)),
            format_upper_case(remove_spaces(area)),
            format_dots(remove_spaces(time)),
            g.user,
            datetime.now()))

        MySQL.con.commit()

        return Response(status=211)

    except MySQL.Error as error:
        print(error)
        return  Response(status=411)

def generate_wp_code () -> str:
    MySQL.cursor.execute('SELECT code FROM wp ORDER BY id DESC LIMIT 1')
    code = MySQL.cursor.fetchone()
    if code is None:
        code = 'WP10000001'
    else:
        code = code[0][:2]+ str(int(code[0][2:])+1)
    return code

def generate_wp_dif (list:list) -> float:
    total_dif = 0
    for task in list:
        MySQL.cursor.execute('SELECT dif FROM tasks WHERE task =%s',
        (task,))
        dif = float(MySQL.cursor.fetchone()[0])
        total_dif = dif + total_dif
    return total_dif/len(list)

def generate_wp_vol (areas:list) -> float:
    total_vol = 0
    for area in areas:
        MySQL.cursor.execute('SELECT vol FROM areas WHERE area =%s',
        (area,))
        vol = float(MySQL.cursor.fetchone()[0])
        total_vol = vol + total_vol
    return total_vol/len(areas)

def generate_wp_cpl (areas:list) -> float:
    total_cpl = 0
    for area in areas:
        MySQL.cursor.execute('SELECT cpl FROM areas WHERE area =%s',
        (area,))
        cpl = float(MySQL.cursor.fetchone()[0])
        total_cpl = cpl + total_cpl
    return total_cpl/len(areas)

def get_weights_tasks(project, discipline, station, task)->float:
    MySQL.cursor.execute('SELECT weight FROM tasks WHERE project =%s AND discipline =%s AND station = %s AND task=%s',
    (project,discipline,station,task))
    return float(MySQL.cursor.fetchone()[0])

def get_weights_areas(project, discipline, zone, area)->float:
    MySQL.cursor.execute('SELECT weight FROM areas WHERE project =%s AND discipline =%s AND zone = %s AND area=%s',
    (project,discipline,zone,area))
    return float(MySQL.cursor.fetchone()[0])

def get_project_hours(project):
    MySQL.cursor.execute('SELECT execution_hours FROM projects WHERE code =%s ORDER BY date DESC LIMIT 1',
    (project,))
    return float(MySQL.cursor.fetchone()[0])

def get_subaction_hours(subaction):
    MySQL.cursor.execute('SELECT time FROM projects WHERE subaction_code=%s',
    (subaction),)
    return float(MySQL.cursor.fetchone()[0])


def generate_wp_contracted_time (project, discipline,zone,type,station,subactions:list,areas:list, tasks:list) -> float:
    total_hours = 0
    if type == "DESIGN":
        for area, task in zip(areas, tasks):
            hour = get_project_hours(project)*get_weights_areas(project,discipline,zone,area)*get_weights_tasks(project,discipline,station,task)
            total_hours = hour + total_hours
        return total_hours
    
    for subaction, task in zip(subactions, tasks):
        hour = get_subaction_hours(subaction)*get_weights_tasks(project,discipline,station,task)
        total_hours = hour + total_hours
    return total_hours


def generate_wp_planned (vol,cpl) -> float:
    return float (((vol+cpl)/10)+1)


@bp.route('/generate_wp', methods=['GET','POST'])
def generate_wp():
    data = request.get_json()
    wp_code =  generate_wp_code()
    wp_dif = generate_wp_dif(data['tasks'])
    wp_vol = generate_wp_vol(data['areas'])
    wp_cpl = generate_wp_cpl(data['areas'])
    wp_time = generate_wp_contracted_time(
        data['project'],
        data['discipline'],
        data['zone'],
        data['type'],
        data['station'],
        data['actions'],
        data['areas'],
        data['tasks']            
    )
    return {
        'wp_code': wp_code,
        'wp_dif': wp_dif,
        'wp_vol': wp_vol,
        'wp_cpl': wp_cpl,
        'wp_contracted_time': wp_time,
        'wp_planned_time': wp_time*generate_wp_planned(wp_vol,wp_cpl)
    }
    
@bp.route('/user_level', methods=['GET','POST'])
def user_level():
    data = request.get_json()
    total_level = 0
    for task in data['tasks']:
        MySQL.cursor.execute('SELECT level FROM users_projects WHERE project =%s AND user =%s AND task = %s',(data['project'],data['user'], task))
        level = (MySQL.cursor.fetchone())

        if level is None:
            level = 0
            total_level = level + total_level
        
        else:
            total_level = float(level[0]) + total_level
        
        
    return {'level': total_level/len(data['tasks'])}
