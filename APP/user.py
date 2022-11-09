from flask import render_template, Blueprint, request
from auth import login_required
from flask.views import View

bp = Blueprint('user', __name__, url_prefix='/user')

class User(View):
    methods = ["GET", "POST"]
    decorators = [login_required]

    def __init__(self,model) -> None:
        self.model = model
        self.template = f'/user/{model}.html'

    def dispatch_request(self):
        if request.method == "GET":
            return render_template(self.template)


bp.add_url_rule('/', view_func=User.as_view('/', 'home'))
bp.add_url_rule('/settings', view_func=User.as_view('/settings', 'settings'))
bp.add_url_rule('/report', view_func=User.as_view('/report', 'report'))


