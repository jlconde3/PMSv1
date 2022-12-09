from general.general import MySQLHelper   


def login_data(username):
    """
    Get info user for login.
    :param username: input vaule for user from form.
    """
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT user,password FROM `pms-users`.`users-login` WHERE user = %s ORDER BY id DESC LIMIT 1', (username,))
    user = MySQL.cursor.fetchone()
    MySQL.con.close()
    return user

def login_client(username):
    """
    Get info user client for login.
    :param username: input vaule for user from form.
    """
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT client FROM `pms-users`.`users-client` WHERE user = %s ORDER BY id DESC LIMIT 1', (username,))
    client = MySQL.cursor.fetchone()
    MySQL.con.close()
    return client



def login_rol(username):
    """
    Get info user rol for login.
    :param username: input vaule for user from form.
    """
    MySQL = MySQLHelper()
    MySQL.cursor.execute('SELECT rol FROM `pms-users`.`users-rol` WHERE user = %s ORDER BY id DESC LIMIT 1', (username,))
    rol = MySQL.cursor.fetchone()
    MySQL.con.close()
    return rol