import MySQLdb
import MySQLdb.cursors


# configure_db
def connectToDatabase():
    # Open database connection
    # MySQLdb.connect("Hostname","dbusername","password","dbname")
    db = MySQLdb.connect('localHost', 'root', 'Sharib@1999', 'webmesecure1')
    return db


def addUserToDb(new_user):
    conn = connectToDatabase()
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('''CREATE TABLE users (id VARCHAR(255), name VARCHAR(255),age VARCHAR(255),country VARCHAR(255))''')
    # cursor.execute('SHOW TABLES')
    # for x in cursor:
    #    print(x)

    # Execute the SQL command
    try:
        sql = "INSERT INTO users (id,name,age,country) VALUES (%s, %s,%s, %s)"
        val = (new_user['id'], new_user['name'],
               new_user['age'], new_user['country'])
        cursor.execute(sql, val)
        conn.commit()

        print(cursor.rowcount, "record inserted.")

    except MySQLdb.Error as e:
        print(e)

    finally:
        # disconnect from server
        conn.close()



def showUsersFromDb():
    conn = connectToDatabase()
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)

    # Execute the SQL command
    try:
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        usersList = cursor.fetchall()

        print(usersList)

        return usersList
    except MySQLdb.Error as e:
        print(e)

    finally:
        # disconnect from server
        conn.close()
