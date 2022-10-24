import os

from dotenv import load_dotenv
from mysql.connector import MySQLConnection, Error

class MySQLHelper(object):
    """
    Establish a connection to database. Returns a connector object. 
    """
    def __init__(self):
        load_dotenv()
        mysql_host = os.getenv("MYSQL_AZURE_HOST")
        mysql_port= os.getenv("MYSQL_AZURE_PORT")
        mysql_user = os.getenv("MYSQL_AZURE_USER")
        mysql_password = os.getenv("MYSQL_AZURE_PASSWORD")
        mysql_database = "web_app"
        mysql_certificate = os.getenv("MYSQL_AZURE_SSL_CA")

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