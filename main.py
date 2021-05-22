import falcon
import pymysql

class Database:
    def getDBconn(ip, usr, paswd, charset, curtype):
        sqlCon  = pymysql.connect(host=ip, user=usr, password=paswd, charset=charset, cursorclass=curtype);
        return sqlCon;

    def createUser(cursor, userName, password,querynum=0, updatenum=0, connection_num=0):
        try:
            sqlCreateUser = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';"%(userName, password);
            cursor.execute(sqlCreateUser);
        except Exception as Ex:
            print("Error creating MySQL User: %s"%(Ex));
    
    # Connection credentials
    ip         = "127.0.0.1";
    usr        = "root";        
    paswd      = "pass";            
    charset    = "utf8mb4";     
    curtype    = pymysql.cursors.DictCursor;    

    mySQLConnection = getDatabaseConnection(ip, usr, paswd, charset, curtype);
    mySQLCursor     = mySQLConnection.cursor();

    createUser(mySQLCursor, "test1","a$be@ter12");
    createUser(mySQLCursor, "test2", "x@ye@iog43"); 

    mySqlListUsers = "select host, user from mysql.user;";
    mySQLCursor.execute(mySqlListUsers);

print("List of users:");
for user in userList:
    print(user);
    
class QuoteResource:
    def on_get(self, req, resp):
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = quote

api = falcon.API()
api.add_route('/quote', QuoteResource())

# get all users
userList = mySQLCursor.fetchall();
