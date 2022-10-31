from common import MySQL, format_upper_case, format_dots, remove_spaces, format_mysql_list
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


@bp.route('/projects',methods=['POST','GET'])
def projects ():
    MySQL.cursor.execute('SELECT DISTINCT project FROM pms.areas')
    return format_mysql_list(MySQL.cursor.fetchall())

@bp.route('/disciplines',methods=['POST','GET'])
def disciplines ():
    data = request.get_json()
    MySQL.cursor.execute('SELECT DISTINCT discipline FROM pms.areas WHERE project = %s', (data['project_code'],))
    return format_mysql_list(MySQL.cursor.fetchall())

@bp.route('/phases',methods=['POST','GET'])
def phases ():
    data = request.get_json()
    MySQL.cursor.execute('SELECT DISTINCT phase FROM pms.areas WHERE project = %s AND discipline = %s',
    (data['project_code'],data['discipline_code']))
    return format_mysql_list(MySQL.cursor.fetchall())

@bp.route('/zones',methods=['POST','GET'])
def zones ():
    data = request.get_json()
    MySQL.cursor.execute('SELECT DISTINCT zone FROM pms.areas WHERE project = %s AND discipline = %s AND phase = %s',
    (data['project_code'],data['discipline_code'],data['phase_code']))
    return format_mysql_list(MySQL.cursor.fetchall())

@bp.route('/areas',methods=['POST','GET'])
def areas ():
    data = request.get_json()
    print(data)
    MySQL.cursor.execute('SELECT DISTINCT area FROM pms.areas WHERE project = %s AND discipline = %s AND phase = %s AND zone = %s',
    (data['project_code'],data['discipline_code'],data['phase_code'],data['zone_code']))
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
            'INSERT INTO pms.projects (agresso_code,date,name,client,section,\
            division,budget,profit_margin,cpt_default,cpt_actions,management,extra,user)VALUES\
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

@bp.route('/create_action', methods=['POST'])
def create_action():
    data = request.get_json()
    try:
        for code,zone, area, time in zip(data['custom_code'],
        data['subaction_zone'],data['subaction_area'], data['subaction_time']):

            MySQL.cursor.execute(
            'INSERT INTO pms.actions (project,customer_code,type,date_recived,\
            disicipline,phase,description,custom_code,zone,area,time,user,date)\
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
            format_upper_case(remove_spaces(data['project_code'])),
            format_upper_case(remove_spaces(data['customer_code'])),
            format_upper_case(remove_spaces(data['action_type'])),
            format_upper_case(data['action_date']),
            format_upper_case(remove_spaces(data['discipline_code'])),
            format_upper_case(remove_spaces(data['phase_code'])),
            format_upper_case(remove_spaces(data['action_description'])),
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