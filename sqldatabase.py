from mysql_parameters import MySQLParameters as pr


def get_connection_string():
    return 'mysql://:' + pr.username + '/' + pr.password + '/' + pr.db_endpoint + '/' + pr.db_instance
