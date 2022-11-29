import json
import csv
import os

from flask import render_template, Blueprint, request, make_response
from auth import login_required
from common import MySQLHelper, InputClass




bp = Blueprint('external_tools', __name__, url_prefix='/external_tools')

@bp.route('/cruscotto', methods=['GET','POST'])
@login_required
def cruscotto():
    if request.method =='GET':
        return render_template('/external_tools/cruscotto/cruscotto.html')
    else:
        file_input = request.files['file']

        file = open(file_input)

        csvreader = csv.reader(file, delimiter=";")

        for row in csvreader:
            print(row)



