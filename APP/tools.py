
from common import MySQL, format_upper_case, format_dots, response
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


@bp.route('/create_project', methods=['POST'])
def create_project():
    data = request.get_json()
    try:
        MySQL.cursor.execute(
            '''
            INSERT INTO pms.projects (agresso_code,date,name,client,section,
            division,budget,profit_margin,cpt_default,cpt_actions,management,extra,user)VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
            (format_upper_case(data['project_code']),
            datetime.now(),
            format_upper_case(data['project_name']),
            format_upper_case(data['project_client']),
            format_upper_case(data['project_section']),
            format_upper_case(data['project_division']),
            format_dots(data['project_budget']),
            format_dots(data['project_profit_margin']),
            format_dots(data['project_cpt']),
            format_dots(data['project_cpt_actions']),
            format_dots(data['project_management_cost']),
            format_dots(data['project_extra_cost']), g.user)
        )
        MySQL.con.commit()
        return Response(status=211)
    except MySQL.Error as error:
        print(error)
        return  Response(status=411)