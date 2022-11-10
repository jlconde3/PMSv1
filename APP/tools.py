
from hashlib import sha256
from common import MySQLHelper , format_upper_case, format_dots, remove_spaces, format_mysql_list, format_actions_list
from flask import render_template, Blueprint, request,g, Response, make_response
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
@login_required
def projects ():
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT DISTINCT project FROM pms.areas')
    data_to_send = format_mysql_list(MySQL.cursor.fetchall())
    MySQL.con.close()
    return data_to_send


@bp.route('/disciplines',methods=['GET','POST'])
@login_required
def disciplines ():
    data = request.get_json()
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT DISTINCT discipline FROM pms.areas WHERE project = %s',
    (remove_spaces(format_upper_case(data['project_code'])),))
    data_to_send = format_mysql_list(MySQL.cursor.fetchall())
    MySQL.con.close()
    return data_to_send

@bp.route('/phases',methods=['GET','POST'])
@login_required
def phases ():
    data = request.get_json()
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT DISTINCT phase FROM pms.areas WHERE project = %s AND\
    discipline = %s',
    (remove_spaces(format_upper_case(data['project_code'])),
    remove_spaces(format_upper_case(data['discipline_code']))
    ))
    data_to_send = format_mysql_list(MySQL.cursor.fetchall())
    MySQL.con.close()
    return data_to_send

@bp.route('/zones',methods=['GET','POST'])
@login_required
def zones ():
    data = request.get_json()
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT DISTINCT zone FROM pms.areas WHERE project = %s AND discipline = %s AND phase = %s',
    (remove_spaces(format_upper_case(data['project_code'])),
    remove_spaces(format_upper_case(data['discipline_code'])),
    remove_spaces(format_upper_case(data['phase_code']))
    ))
    data_to_send = format_mysql_list(MySQL.cursor.fetchall())
    MySQL.con.close()
    return data_to_send

@bp.route('/areas',methods=['GET','POST'])
@login_required
def areas ():
    data = request.get_json()
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT DISTINCT area FROM pms.areas WHERE project = %s AND discipline = %s AND phase = %s AND zone = %s',
    (remove_spaces(format_upper_case(data['project_code'])),
    remove_spaces(format_upper_case(data['discipline_code'])),
    remove_spaces(format_upper_case(data['phase_code'])),
    remove_spaces(format_upper_case(data['zone_code']))
    ))
    data_to_send = format_mysql_list(MySQL.cursor.fetchall())
    MySQL.con.close()
    return data_to_send

@bp.route('/actions',methods=['GET','POST'])
@login_required
def actions ():
    data = request.get_json()
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT subaction_code, custom_code FROM pms.actions WHERE project = %s AND discipline = %s AND phase = %s AND zone = %s AND status = "Not assigned" ',
    (remove_spaces(format_upper_case(data['project_code'])),
    remove_spaces(format_upper_case(data['discipline_code'])),
    remove_spaces(format_upper_case(data['phase_code'])),
    remove_spaces(format_upper_case(data['zone_code'])) 
    ))
    data_to_send = format_mysql_list(MySQL.cursor.fetchall())
    MySQL.con.close()
    return data_to_send

@bp.route('/actions_stations',methods=['GET','POST'])
@login_required
def actions_stations ():
    data = request.get_json()
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT DISTINCT station FROM pms.tasks WHERE project = %s AND discipline = %s AND line ="ACTIONS"',
    (remove_spaces(format_upper_case(data['project_code'])),
    remove_spaces(format_upper_case(data['discipline_code'])),
    ))
    data_to_send = format_mysql_list(MySQL.cursor.fetchall())
    MySQL.con.close()
    return data_to_send

@bp.route('/lines',methods=['GET','POST'])
@login_required
def types ():
    data = request.get_json()
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT DISTINCT line FROM pms.tasks WHERE project = %s AND discipline=%s',
    (remove_spaces(format_upper_case(data['project_code'])), remove_spaces(format_upper_case(data['discipline_code']))))
    data_to_send = format_mysql_list(MySQL.cursor.fetchall())
    MySQL.con.close()
    return data_to_send

@bp.route('/stations',methods=['GET','POST'])
@login_required
def stations ():
    data = request.get_json()
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT DISTINCT station FROM pms.tasks WHERE project = %s AND discipline = %s AND line =%s',
    (remove_spaces(format_upper_case(data['project_code'])),
    remove_spaces(format_upper_case(data['discipline_code'])),
    remove_spaces(format_upper_case(data['wp_line']))
    ))
    data_to_send = format_mysql_list(MySQL.cursor.fetchall())
    MySQL.con.close()
    return data_to_send

@bp.route('/tasks',methods=['GET','POST'])
@login_required
def tasks ():
    data = request.get_json()
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT DISTINCT task FROM pms.tasks WHERE project=%s AND discipline=%s AND line=%s AND station=%s',
    (remove_spaces(format_upper_case(data['project_code'])),
    remove_spaces(format_upper_case(data['discipline_code'])),
    remove_spaces(format_upper_case(data['wp_line'])),
    remove_spaces(format_upper_case(data['station_code']))
    ))
    data_to_send = format_mysql_list(MySQL.cursor.fetchall())
    MySQL.con.close()
    return data_to_send

@bp.route('/users_projects',methods=['GET','POST'])
@login_required
def users_projects():
    data = request.get_json()
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT DISTINCT user FROM pms.users_projects WHERE project = %s',
    (remove_spaces(format_upper_case(data['project_code'])),))
    data_to_send = format_mysql_list(MySQL.cursor.fetchall())
    MySQL.con.close()
    return data_to_send

@bp.route('/create_project', methods=['POST'])
@login_required
def create_project():
    data = request.get_json()
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT DISTINCT code FROM pms.projects WHERE agresso_code = %s', (format_upper_case(remove_spaces(data['project_code'])),)) 

    if MySQL.cursor.fetchone() is not None:
        return  Response(status=215)

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
        MySQL.con.close()

        return Response(status=211)

    except MySQL.Error as error:
        MySQL.con.close()
        print(error)
        return  Response(status=411)


def generate_action_code () -> str:
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT action_code FROM actions ORDER BY id DESC LIMIT 1')
    code = MySQL.cursor.fetchone()
    if code is None:
        code = 'ACT1000001'
    else:
        code = code[0][:3]+ str(int(code[0][3:])+1)
    return code

def generate_subaction_code () -> str:
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT subaction_code FROM actions ORDER BY id DESC LIMIT 1')
    code = MySQL.cursor.fetchone()
    MySQL.con.close()
    if code is None:
        code = 'SUBACT10000001'
    else:
        code = code[0][:6]+ str(int(code[0][6:])+1)
    return code


@bp.route('/create_action', methods=['POST'])
@login_required
def create_action():
    MySQL = MySQLHelper()
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
        MySQL.con.close()

        return Response(status=211)

    except MySQL.Error as error:
        MySQL.con.close()
        print(error)
        return  Response(status=411)

def generate_wp_code () -> str:
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT code FROM wp ORDER BY id DESC LIMIT 1')
    code = MySQL.cursor.fetchone()
    if code is None:
        code = 'WP10000001'
    else:
        code = code[0][:2]+ str(int(code[0][2:])+1)
    MySQL.con.close()
    return code

def generate_wp_dif (list:list) -> float:
    total_dif = 0
    MySQL = MySQLHelper()
    for task in list:
        MySQL.cursor.execute('SELECT dif FROM tasks WHERE task =%s',
        (task,))
        dif = float(MySQL.cursor.fetchone()[0])
        total_dif = dif + total_dif

    MySQL.con.close()
    return total_dif/len(list)

def generate_wp_vol (areas:list) -> float:
    total_vol = 0
    MySQL = MySQLHelper()
    for area in areas:
        MySQL.cursor.execute('SELECT vol FROM areas WHERE area =%s',
        (area,))
        vol = float(MySQL.cursor.fetchone()[0])
        total_vol = vol + total_vol
    MySQL.con.close()
    return total_vol/len(areas)

def generate_wp_cpl (areas:list) -> float:
    total_cpl = 0
    MySQL = MySQLHelper()
    for area in areas:
        MySQL.cursor.execute('SELECT cpl FROM areas WHERE area =%s',
        (area,))
        cpl = float(MySQL.cursor.fetchone()[0])
        total_cpl = cpl + total_cpl
    return total_cpl/len(areas)

def get_weights_tasks(project, discipline, station, task)->float:
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT weight FROM tasks WHERE project =%s AND discipline =%s AND station = %s AND task=%s',(project,discipline,station,task))
    data_to_send = float(MySQL.cursor.fetchone()[0])
    MySQL.con.close()
    return data_to_send

def get_weights_areas(project, discipline, zone, area)->float:
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT weight FROM areas WHERE project =%s AND discipline =%s AND zone = %s AND area=%s',(project,discipline,zone,area))
    data_to_send = float(MySQL.cursor.fetchone()[0])
    MySQL.con.close()
    return data_to_send

def get_project_hours(project):
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT execution_hours FROM projects WHERE code =%s ORDER BY date DESC LIMIT 1',(project,))
    data_to_send = float(MySQL.cursor.fetchone()[0])
    MySQL.con.close()
    return data_to_send

def get_subaction_hours(subaction):
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT time FROM actions WHERE subaction_code=%s',(subaction,))
    data_to_send = float(MySQL.cursor.fetchone()[0])
    MySQL.con.close()
    return data_to_send


def generate_wp_contracted_time (project, discipline, wp_line, station, zone, areas:list, subactions:list, tasks:list) -> float:

    total_hours = 0

    if wp_line == "DESIGN":
        for area, task in zip(areas, tasks):
            hour = get_project_hours(project)*get_weights_areas(project,discipline,zone,area)*get_weights_tasks(project,discipline,station,task)
            total_hours = hour + total_hours
        return total_hours
    
    for subaction, task in zip(subactions, tasks):
        hour = get_subaction_hours(subaction)*get_weights_tasks(project,discipline,station,task)
        total_hours = hour + total_hours

    return total_hours

def generate_wp_planned_time (vol,cpl) -> float:
    return float (((vol+cpl)/10)+1)

def validate_combination (project:str, discipline:str, phase:str,wp_line:str, station:str, zone:str, area:str, action:str, task:str)->bool:
    """
    Check if a combination of project, discipline, phase, wp_line, station, zone, area, action, task area unique.

    Return True if combination is unique, False if it is repeated.
    """

    text_to_hash = f"{project}{discipline}{phase}{wp_line}{station}{zone}{area}{action}{task}"
    id = sha256(text_to_hash.encode('utf-8')).hexdigest()
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT * FROM wp WHERE id_hash = %s',(id,))
    check = MySQL.cursor.fetchall()
    MySQL.con.close()
    return True if check == [] else False

def generate_wp_id(project:str, discipline:str, phase:str, wp_line:str,station:str, zone:str, area:str, action:str, task:str)->str:
    """
    Generate a unique id for each combination.

    Returns sha256 string.
    """

    text_to_hash = f"{project}{discipline}{phase}{wp_line}{station}{zone}{area}{action}{task}"
    id = sha256(text_to_hash.encode('utf-8')).hexdigest()
    return id

@bp.route('/generate_wp', methods=['GET','POST'])
@login_required
def generate_wp():
    data = request.get_json()
    project = str(data ['project'])
    discipline = data ['discipline']
    phase = data ['phase']
    zone = data ['zone']
    wp_line = data ['wp_line']
    station = data ['station']
    areas_list = []
    actions_list = []
    tasks_list = data ['tasks']
    
    
    check_all = True

    if check_input_value('SELECT DISTINCT project FROM areas',project):        
        sql = [
            (f"SELECT DISTINCT discipline FROM areas WHERE project='{project}'"),
            (f"SELECT DISTINCT phase FROM areas WHERE project='{project}'"),
            (f"SELECT DISTINCT zone FROM areas WHERE project='{project}'"),
            (f"SELECT DISTINCT line FROM tasks WHERE project='{project}'"),
            (f"SELECT DISTINCT station FROM tasks WHERE project='{project}'")
        ]
        values = [discipline,phase,zone,wp_line,station]

        for i,j in zip(sql,values):
            if check_input_value(i,j) is False:
                check_all = False
                break
        
    else:
        check_all = False

    

    if check_all:
        if wp_line == "DESIGN":
            areas_list = data ['areas']

            for i in areas_list:
                if check_input_value(f"SELECT DISTINCT area FROM areas WHERE project='{project}'",i) is False:
                    check_all = False
                    break
            
            if check_all:
                for area, task in zip(areas_list,tasks_list):
                    if validate_combination (project, discipline, phase,
                                            wp_line, station, zone, area, "", task) is False:
                        unique = False
                        break
                    else:
                        unique = True

                if not unique:
                    response = make_response({
                    'area':area,
                    'task':task
                    }, 212)
                    return response

                wp_code =  generate_wp_code()
                wp_dif = generate_wp_dif(tasks_list)
                wp_vol = generate_wp_vol(areas_list)
                wp_cpl = generate_wp_cpl(areas_list)
                wp_time = generate_wp_contracted_time(project, discipline, wp_line, station, zone, areas_list, [], tasks_list)

                response = make_response({
                'wp_code': wp_code,
                'wp_dif': wp_dif,
                'wp_vol': wp_vol,
                'wp_cpl': wp_cpl,
                'wp_contracted_time': wp_time,
                'wp_planned_time': generate_wp_planned_time(wp_vol, wp_cpl)*wp_time
                }, 213)

                return response

        elif wp_line == "ACTIONS":

            actions_list = data ['actions']
            subaction_list = []

            for i in actions_list:
                subaction = i.split('-')
                subaction_list.append(subaction[0])
                MySQL.cursor.execute('SELECT area FROM actions WHERE project =%s AND subaction_code = %s',(data['project'], subaction[0]))
                area = (MySQL.cursor.fetchone())
                areas_list.append(area[0])
        
            for area,action, task in zip(areas_list,subaction_list,tasks_list):
                if validate_combination (project, discipline, phase, wp_line, station, zone, area, action, task) is False:
                    print("Not unique")
                    unique = False
                    break
                else:
                    print("Unique")
                    unique = True

            if not unique:
                response = make_response({
                'area':area,
                'task':task
                }, 212)
                return response

            wp_code =  generate_wp_code()
            wp_dif = generate_wp_dif(tasks_list)
            wp_vol = generate_wp_vol(areas_list)
            wp_cpl = generate_wp_cpl(areas_list)
            wp_time = generate_wp_contracted_time(project, discipline, wp_line, station, zone, areas_list, subaction_list, tasks_list)

            response = make_response({
            'wp_code': wp_code,
            'wp_dif': wp_dif,
            'wp_vol': wp_vol,
            'wp_cpl': wp_cpl,
            'wp_contracted_time': wp_time,
            'wp_planned_time': generate_wp_planned_time(wp_vol, wp_cpl)*wp_time
            }, 213)

            return response

    return make_response({'response':"Incorrect values"},220)

@bp.route('/user_level', methods=['GET','POST'])
@login_required
def user_level():
    data = request.get_json()
    total_level = 0
    MySQL = MySQLHelper()
    for task in data['tasks']:
        MySQL.cursor.execute('SELECT level FROM users_projects WHERE project =%s AND user =%s AND task = %s',(data['project'],data['user'], task))
        level = (MySQL.cursor.fetchone())

        if level is None:
            level = 0
            total_level = level + total_level
        
        else:
            total_level = float(level[0]) + total_level
        
    MySQL.con.close()
    return {'level': total_level/len(data['tasks'])}

@bp.route('/validate_wp', methods=['GET','POST'])
@login_required
def validate_wp():
    data = request.get_json()
    project = data ['project_code']
    discipline = data ['discipline_code']
    phase = data ['phase_code']
    wp_line = data ['wp_line']
    station = data ['wp_station']
    zone = data ['wp_zone']
    actions_list = data ['task_action']
    areas_list = data ['task_area']
    tasks_list = data ['task_code']
    wp_code = data ['wp_code']
    dif = data ['wp_difficulty']
    vol = data ['wp_volume']
    cpl = data ['wp_complexity']
    wp_contracted = data ['wp_contracted_time']
    wp_planned = data ['wp_planned_time']
    wp_scheduled = data ['wp_scheduled_time']
    users = data ['username']
    users_level = data ['user_level']

    try:
        MySQL = MySQLHelper()
        for action, area, task in zip(actions_list, areas_list, tasks_list):
            id_hash = generate_wp_id(project, discipline, phase, wp_line, station, zone, area, action, task)
            MySQL.cursor.execute("""
            INSERT INTO wp(code,id_hash,project,discipline,phase,zone,line,station,action,area,
            task,dif,vol,cpl,contacted_time,planned_time,scheduled_time)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
            """,(wp_code,id_hash,project,discipline,phase,zone,wp_line,station,action,area,task,dif,vol,cpl,wp_contracted,wp_planned,wp_scheduled))

        for user in users:
            MySQL.cursor.execute("""INSERT INTO users_wp(user,project,wp,scheduled_time)VALUES(%s,%s,%s,%s)""",(user,project,wp_code,float(wp_scheduled)/len(users)))
            
        MySQL.con.commit()
        MySQL.con.close()
        return Response(status=211)

    except MySQL.Error as e:
        MySQL.con.close()
        print(e)
        return Response(status=411)


@bp.route('/action_area', methods=['GET','POST'])
@login_required
def action_area():
    data = request.get_json()
    project = data['project']
    action = str (data['action'])
    action_code = action.split('-')
    

    try:
        MySQL = MySQLHelper()
        MySQL.cursor.execute("""SELECT area FROM actions WHERE project =%s AND subaction_code =%s""", (project,action_code[0]))
        area = MySQL.cursor.fetchone()[0]
        MySQL.con.close()
        response = make_response({'area':area}, 211)
        return response

    except MySQL.Error as e:
        print(e)
        response = make_response({'response':e}, 411)
        return response

def check_input_type (value,type) -> bool:
    if type(value) == type:
        return True
    return False


def check_input_value(mysql_sentence:str,input_value:str) -> bool:
    values_list = []
    MySQL = MySQLHelper()
    MySQL.cursor.execute(mysql_sentence)
    values = MySQL.cursor.fetchall()
    MySQL.con.close()
    for i in values:
        values_list.append(i[0])

    if input_value in values_list:
        return True
    
    return False


