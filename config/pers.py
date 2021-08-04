import mysql

def mysql_conn(**config):
    """
    Exemple of method to connect with a MySQL DB if the business establishment/store had one
    """

    connection = mysql.connector.connect(
        host='192.168.2.1/bakery/server2',
        database='defaultDB',
        user='johndoe123',
        password='321anypassword'
    )

    return connection
