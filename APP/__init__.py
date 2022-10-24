from wsgi import create_app

create_app().run('0.0.0.0', 5002, debug=True)