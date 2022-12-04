import os 
import sys

from flask import Flask

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='7NN@j14wh*5B',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    sys.path.append( os.path.join(os.path.dirname(sys.path[0]),'PMSv3/APP'))


    from auth import auth
    app.register_blueprint(auth.bp)

    from general import general

    from tools import tools
    app.register_blueprint(tools.bp)

    from projects import projects
    app.register_blueprint(projects.bp)

    from actions import actions
    app.register_blueprint(actions.bp)

    from wps import wps 
    app.register_blueprint(wps.bp)

    from kanban import kanban
    app.register_blueprint(kanban.bp)

    from data import data
    app.register_blueprint(data.bp)

    from user import user
    app.register_blueprint(user.bp)




    return app

