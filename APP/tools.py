from flask import render_template, Blueprint, request
from auth import login_required
from flask.views import View

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
    print(data)
    return "Hola"

@bp.route('/create_action', methods=['POST'])
def create_action():
    data = request.get_json()
    print(data)
    return "Hola"

@bp.route('/create_wp', methods=['POST'])
def create_wp():
    data = request.get_json()
    print(data)
    return "Hola"

@bp.route('/projects', methods=['POST'])
def retrive_projects():
    return ['Hola', 'me','llamo','jose']

@bp.route('/disciplines', methods=['POST'])
def retrive_disciplines():
    data = request.get_json()
    if data['project_code'] == "Hola":
        return ['me','llamo','jose']
    
    return[1,2,3]