import mysql.connector

class DBUtil:
    @staticmethod
    def getDBConn():
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="HMBank",
                port="3306"
            )
            print("Connected to MySQL database")
            return connection
        except mysql.connector.Error as err:
            print("Error:", err)
