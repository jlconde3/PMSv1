import os
import re

from dotenv import load_dotenv
from mysql.connector import MySQLConnection, Error
from flask.views import View


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
    def __init__(self,input_value) -> None:
        self.value = input_value
        self.type = type(input_value)

    def check_for_sensitive_chars(self)->bool:
        '''
        Check for sensitive characters in a string.

        :param data: string to check.
        Returns false if string has sensitive chars and true if not.
        '''

        if re.search("[^0-9A-Za-zÀ-ÿ-.,@Ññ ]+",self.value) is None:
            return True
        return False

    def check_for_digits(self)->bool:
        '''
        Check for numbers in a string.

        :param data: string to check.
        Returns false if a string has letters and true if not.
        '''

        if re.search("[^0-9.,]+",self.value) is None:
            return True
        return False

    def check_correct_format_numbers(self)->bool:
        '''
        Check for the correct format of numbers.

        :param data: string to check.
        Returns True if a string do start with "." or ",".False if not.
        '''

        if re.search("^[.,]+",self.value) is None:
            return True
        return False
    
    def check_input_value(self,MySQL:object,field:str,table:str,proejct:str)-> bool:
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
        MySQL.cursor.execute(f"SELECT DISTINCT {field} FROM {table} WHERE project = '{proejct}'")
        reponse = MySQL.cursor.fetchall()

        #Create and empty list and save data to be compared.
        whitelist = []
        
        for i in reponse:whitelist.append(i[0])

        #If value is not in whitelist return false or true.
        return True if self.value in whitelist else False
    

    def format_upper_case (self:str)->str:
        '''
        Format string to uppercase.

        :param data: string to format.
        Returns format string.
        '''
        return self.value.upper()

    def remove_spaces (self:str)->str:
        ''' 
        Remove unnecesary white space from strings.

        :param self: string to format.
        Returns format string.
        '''
        return self.value.replace(" ","")
    
    def replace_comma_for_dot(self:str)->float:
        ''' 
        Replace commas for dots for numerical fields.

        :param self: string to format.
        Returns float number.
        '''
        return float (self.value.replace(",","."))
