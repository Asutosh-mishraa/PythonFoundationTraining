from util.PropertyUtil import PropertyUtil
import mysql.connector


class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            connection_parameters = PropertyUtil.getPropertyString()
            DBConnection.connection = mysql.connector.connect(**connection_parameters)
            if DBConnection.connection.is_connected():
                print("Connected to MySQL database")
        return DBConnection.connection


# con = DBConnection.getConnection()
# cur = con.cursor()
# cur.execute("show tables")
# res = cur.fetchall()
# for i in res:
#     print(i)
# con.close()
