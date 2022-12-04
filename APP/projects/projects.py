import json

from flask import render_template, Blueprint, request,g, make_response, redirect, url_for
from common import MySQLHelper,InputClass
from auth import login_required, CustomViews
from decimal import Decimal
from datetime import datetime

bp = Blueprint('projects', __name__, url_prefix='/projects')

bp.add_url_rule('/create_project', view_func=CustomViews.as_view('/create_proejct','/tools/projects/create_project.html'))
bp.add_url_rule('/modify_project', view_func=CustomViews.as_view('/modify_project','/tools/projects/modify_project.html'))

@bp.route('/create', methods=['POST'])
@login_required
def create ():
    code = InputClass(request.form['code'])
    name = InputClass(request.form['name'])
    client = InputClass(request.form['client'])
    section = InputClass(request.form['section'])
    division = InputClass(request.form['division'])
    budget = InputClass(request.form['budget'])
    margin = InputClass(request.form['margin'])
    default = InputClass(request.form['default'])
    action = InputClass(request.form['actions'])
    management = InputClass(request.form['management'])
    others = InputClass(request.form['others'])

    error = None
    
    if error is None:
        for i in [code,name,client,section, division, budget,margin, default,action, management,others]:
            if not i.check_for_sensitive_chars():
                error = make_response(f'Special char not allowed: {i.value}',401)
                break
            
    if error is None:
        for i in [margin, default,action, management, others]:
            if not i.check_for_digits():
                error = make_response(f'Incorrect format:{i.value}',401)
                break

    if error is None:
        exc_budget = float(budget.value)*(1-float(margin.value))
        management_hours = exc_budget*float(management.value)/float(default.value)
        others_hours = exc_budget*float(others.value)/float(default.value)
        work_hours = (exc_budget/float(default.value)-management_hours-others_hours)

        MySQL = MySQLHelper()

        MySQL.cursor.execute('SELECT DISTINCT code FROM projects')
        values = MySQL.cursor.fetchall()

        projects = []
        for i in values:projects.append(i[0])
        
        if not code.value in projects:
            MySQL.cursor.execute("""
                INSERT INTO projects(code,date,name,client,section,
                division,budget,profit_margin,cpt_default,cpt_actions,
                management,extra,user,execution_budget,execution_hours,management_hours,others_hours)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                (code.value,datetime.today(),name.value,client.value,section.value,
                division.value,budget.value,margin.value,default.value,action.value,
                management.value,others.value,g.user,exc_budget,work_hours,management_hours,others_hours))
            MySQL.con.commit()
            MySQL.con.close()
            return redirect(url_for('tools./'))

        MySQL.con.close()
        error = make_response(f'Project {code} already exist',401)

    return error

@bp.route('/retrive_data', methods=['POST'])
@login_required
def retrive_data():
    
    data = request.get_json()
    code = InputClass(data['code'])
     
    if not code.check_for_sensitive_chars():
        return make_response(f'Special char not allowed: {code.value}',401)

    MySQL = MySQLHelper()
    MySQL.cursor.execute("SELECT DISTINCT code FROM projects")
    projects_sql = MySQL.cursor.fetchall()

    projects = []
    for i in projects_sql:projects.append(i[0])

    if code.value in projects:
        MySQL.cursor.execute("SELECT * FROM projects WHERE code =%s ORDER BY date DESC LIMIT 1",(code.value,))
        response = MySQL.cursor.fetchone()

        row_data = []
        for value in response:
            if type(value) is Decimal:
                row_data.append(float(value))
            else:
                row_data.append(str(value))

        MySQL.con.close()    
        return json.dumps({'response':row_data})

    MySQL.con.close()    
    return make_response(f'Project {code} not found',401)



        
@bp.route('/modify', methods=['POST'])
@login_required
def modify ():
    code = InputClass(request.form['code'])
    name = InputClass(request.form['name'])
    client = InputClass(request.form['client'])
    section = InputClass(request.form['section'])
    division = InputClass(request.form['division'])
    budget = InputClass(request.form['budget'])
    margin = InputClass(request.form['margin'])
    default = InputClass(request.form['default'])
    action = InputClass(request.form['actions'])
    management = InputClass(request.form['management'])
    others = InputClass(request.form['others'])

    error = None
    
    if error is None:
        for i in [code,name,client,section,division,budget,margin,default,action,management,others]:
            if not i.check_for_sensitive_chars():
                error = make_response(f'Special char not allowed: {i.value}',401)
                break
            
    if error is None:
        for i in [margin,default,action,management,others]:
            if not i.check_for_digits():
                error = make_response(f'Incorrect format:{i.value}',401)
                break

    if error is None:
        exc_budget = float(budget.value)*(1-float(margin.value))
        management_hours = exc_budget*float(management.value)/float(default.value)
        others_hours = exc_budget*float(others.value)/float(default.value)
        work_hours = (exc_budget/float(default.value)-management_hours-others_hours)

        MySQL = MySQLHelper()
        MySQL.cursor.execute("""
            INSERT INTO projects(code,date,name,client,section,
            division,budget,profit_margin,cpt_default,cpt_actions,
            management,extra,user,execution_budget,execution_hours,management_hours,others_hours)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (code.value,datetime.today(),name.value,client.value,section.value,
            division.value,budget.value,margin.value,default.value,action.value,
            management.value,others.value,g.user,exc_budget,work_hours,management_hours,others_hours))
        MySQL.con.commit()
        MySQL.con.close()
        
        return redirect(url_for('tools./'))

    return error




        
    



