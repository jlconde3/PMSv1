import json
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

MySQL = MySQLHelper()


def format_upper_case (data:str)->str:
    '''
    Format string to uppercase.

    :param data: string to format.

    Returns format string.
    '''
    return data.upper()

def format_dots (data:str)->str:
    ''' 
    replace commas for dots in numeric strings.

    :param data: string to format.
    
    Returns format string.
    '''
    return data.replace(',','.')

def remove_spaces (data:str)->str:
    ''' 
    Remove non-informative white space from strings.

    :param data: string to format.
    
    Returns format string.
    '''
    return data.replace(" ","")


def format_mysql_list(list:list)->list:
    empty_list = []
    for i in list:
        empty_list.append(i[0])
    return empty_list
