import mysql.connector

from util.PropertyUtil import PropertyUtil


class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            connection_parameters = PropertyUtil.getPropertyString()
            DBConnection.connection = mysql.connector.connect(**connection_parameters)
            # if DBConnection.connection.is_connected():
            #     print("Connected to MySQL database")
        return DBConnection.connection

# con = DBConnection.getConnection()
# cursor = con.cursor()
# cur.execute("show tables")
# res = cur.fetchall()
# for i in res:
#     print(i)
# con.close()
# sql = "SELECT * FROM Artwork WHERE ArtworkID = %s"
# cursor.execute(sql, (1,))
# artwork_data = cursor.fetchone()
# print(artwork_data)