import os

from dotenv import load_dotenv
from mysql.connector import MySQLConnection, Error

class MySQLHelper(object):
    '''
    Class for connection to database. 

    Returns a connector object. 
    '''
    def __init__(self):
        load_dotenv()
        mysql_host = os.getenv('MYSQL_AZURE_HOST')
        mysql_port= os.getenv('MYSQL_AZURE_PORT')
        mysql_user = os.getenv('MYSQL_AZURE_USER')
        mysql_password = os.getenv('MYSQL_AZURE_PASSWORD')
        mysql_database = os.getenv('MYSQL_AZURE_DATABASE')
        mysql_certificate = os.getenv('MYSQL_AZURE_SSL_CA')

        self.con = MySQLConnection(
            user = mysql_user,
            password = mysql_password,
            host = mysql_host, port = mysql_port, 
            database = mysql_database,
            ssl_ca = mysql_certificate, 
            ssl_disabled = False)

        self.cursor = self.con.cursor(buffered=True)
        self.Error = Error


def format_upper_case (data:str)->str:
    '''
    Format string to uppercase.

    :param data: string to format.

    Returns format string.
    '''
    return data.upper()

x




def format_mysql_list(list:list)->list:
    empty_list = []
    for i in list:
        empty_list.append(i[0])
    return empty_list

def format_actions_list(list:list)->list:
    empty_list = []
    for i in list:
        empty_list.append(i[0]+"-"+i[1])
    return empty_list