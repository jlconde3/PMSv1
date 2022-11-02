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

    MySQL.cursor.execute('SELECT DISTINCT agresso_code FROM pms.projects WHERE agresso_code = %s',
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


@bp.route('/generate_wp', methods=['GET','POST'])
def generate_wp():
    pass