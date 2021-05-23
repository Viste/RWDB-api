import falcon
import pymysql

class RWDBAPI:
    def getDBconn(ip, usr, paswd, charset, curtype):
        sqlCon  = pymysql.connect(host=ip, user=usr, password=paswd, charset=charset, cursorclass=curtype);
        return sqlCon;

    def createUser(self, cursor, userName, password, querynum=0, updatenum=0, connection_num=0):
        try:
            sqlCreateUser = "CREATE USER '%s'@'%' IDENTIFIED BY '%s';" % (userName, password)
            cursor.execute(sqlCreateUser)
        except Exception as Ex:
            print("Error creating MySQL User: %s"%(Ex))

        # Connection credentials #TODO: move global
        ip         = "127.0.0.1"
        usr        = "root"
        paswd      = "pass"
        charset    = "utf8mb4"
        curtype    = pymysql.cursors.DictCursor

        mySQLConnection = getDBconn(ip, usr, paswd, charset, curtype)
        mySQLCursor     = mySQLConnection.cursor()

        createUser(mySQLCursor, "test1","a$be@ter12")
        createUser(mySQLCursor, "test2", "x@ye@iog43")
        
        mySqlListUsers = "select host, user from mysql.user;"
        mySQLCursor.execute(mySqlListUsers)
       
        # get all users
        userList = mySQLCursor.fetchall()
        print("List of users:")
        for user in userList:
            print(user)

    def createdb(self, cursor, dbname ,querynum=0, updatenum=0, connection_num=0):
        try:
            sqlCreatedb   = "CREATE DATABASE %s" % (database)
            cursor.execute(sqlCreatedb)
        except Exception as Ex:
            print("Error creating MySQL User: %s"%(Ex))

        # Connection credentials #TODO: move global
        ip         = "127.0.0.1"
        usr        = "root"
        paswd      = "pass"
        charset    = "utf8mb4"
        curtype    = pymysql.cursors.DictCursor

        mySQLConnection = getDBconn(ip, usr, paswd, charset, curtype)
        mySQLCursor     = mySQLConnection.cursor()

        createUser(mySQLCursor, "somedb")
        
        mySqlListdbs = "show databeses;"
        mySQLCursor.execute(mySqlListdbs)
       
        # get all users
        dbList = mySQLCursor.fetchall()
        print("List of databases:")
        for db in dbList:
            print(db)

    def on_post(self, req, resp):
        create = {
        }

        resp.media = create

api = falcon.API()
api.add_route('/create', RWDBAPI())

