import os 
import sys

from flask import Flask, redirect, url_for

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='7NN@j14wh*5B',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    sys.path.append( os.path.join(os.path.dirname(sys.path[0]),'PMSv3/PMS'))

    @app.route("/")
    def init ():
        return redirect(url_for('tools./'))

    import auth
    app.register_blueprint(auth.bp)
    import data
    app.register_blueprint(data.bp)
    import tools
    app.register_blueprint(tools.bp)
    import projects
    app.register_blueprint(projects.bp)
    import actions
    app.register_blueprint(actions.bp)
    import wps
    app.register_blueprint(wps.bp)
    import user
    app.register_blueprint(user.bp)
    import kanban
    app.register_blueprint(kanban.bp)

    return app

