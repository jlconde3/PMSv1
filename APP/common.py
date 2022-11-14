import os
import re
import datetime

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

class InputClass():
    def __init__(self,input_value:str) -> None:
        self.value = input_value.upper().strip()
        self.type = type(input_value)

    def check_input_project(self,MySQL:object)-> bool:
        
        '''
        Check if an input project value match to an existing value.

        :param self: value to check.
        :param MySQL: object to stablish connection to database. 
        Return True if exists or False if not.
        '''
        
        MySQL.cursor.execute("SELECT DISTINCT code FROM projects")
        response = MySQL.cursor.fetchall()

        #Create and empty list and save data to be compared.
        whitelist = []
        
        for i in response:whitelist.append(i[0])
            

        #If value is not in whitelist return false or true.
        return True if self.value in whitelist else False

    def check_input_value(self,MySQL:object,field:str,table:str,project:str)-> bool:
        '''
        Check if an input value match to an existing value.

        :param self: value to check.
        :param MySQL: object to stablish connection to database. 
        :param field: field to search in a specific table.
        :param table: table to search.
        :param project: argument to pass to sql_statment.
        Return True if exists or False if not.
        '''
    
        #Retrive data from DB.
        MySQL.cursor.execute(f"SELECT DISTINCT {field} FROM {table} WHERE project = '{project}'")
        response = MySQL.cursor.fetchall()

        #Create and empty list and save data to be compared.
        whitelist = []
        
        for i in response:whitelist.append(i[0])

        #If value is not in whitelist return false or true.
        return True if self.value in whitelist else False

    def check_for_sensitive_chars(self)->bool:
        '''
        Check for sensitive characters in a string.

        :param data: string to check.
        Returns false if string has sensitive chars and true if not.
        '''

        if re.search("[^0-9A-Za-zÀ-ÿ-.,Ññ ]+",self.value) is None:
            return True
        return False

    def check_for_date(self)->bool:
        '''
        Check for date,

        :param data: value to check.
        Returns false if string has sensitive chars and true if not.
        '''
        try:
            datetime.datetime.strptime(self.value,'%Y-%m-%d')
            return True
        except ValueError:
            raise ValueError ("Incorrect data format, should be DD-MM-YYYY")
    
    def check_for_digits(self)->bool:
        '''
        Check for numbers in a string.

        :param data: string to check.
        Returns false if a string has letters and true if not.
        '''
        if re.search("(^\.|\.$)",self.value) is None:
            if re.search("[^\.0-9]",self.value) is None:
                return True
            return False


