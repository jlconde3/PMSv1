import imp
import os 
import sys

from flask import Flask, redirect, url_for, render_template

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    sys.path.append( os.path.join(os.path.dirname(sys.path[0]),'PMSv3/PMS'))

    @app.route("/")
    def init ():
        return redirect(url_for('main.main'))

    import auth
    app.register_blueprint(auth.bp)
    import main
    app.register_blueprint(main.bp)
    import data
    app.register_blueprint(data.bp)
    import wp
    app.register_blueprint(wp.bp)

    return app
