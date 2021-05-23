import falcon
import mysql.connector

config = {
  'user': 'root',
  'password': 'password',
  'host': '127.0.0.1',
  'raise_on_warnings': True
}

class RWDBAPI:
    def createUser(self, cursor, userName, password):
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        try:
            sqlCreateUser = "CREATE USER '%s'@'%' IDENTIFIED BY '%s';" % (userName, password)
            cursor.execute(sqlCreateUser)
        except Exception as Ex:
            print("Error creating MySQL User: %s"%(Ex))

        createUser(cursor, "test1","a$be@ter12")
        createUser(cursor, "test2", "x@ye@iog43")
        
    def createdb(self, cursor, dbname):
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        try:
            sqlCreatedb   = "CREATE DATABASE %s" % (database)
            cursor.execute(sqlCreatedb)
        except Exception as Ex:
            print("Error creating MySQL User: %s"%(Ex))

        createUser(mySQLCursor, "somedb")
        
        mySqlListdbs = "show databeses;"
        cursor.execute(mySqlListdbs)

        databaseList  = mySQLCursor.fetchall()
        for datatbase in databaseList:
            print(datatbase))

    def on_post(self, req, resp):
        create = {
        }

        resp.media = create

api = falcon.API()
api.add_route('/create', RWDBAPI())

