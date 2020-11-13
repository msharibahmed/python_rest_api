import MySQLdb
import MySQLdb.cursors


# configure_db
def connectToDatabase():
    # Open database connection
    # MySQLdb.connect("Hostname","dbusername","password","dbname")
    db = MySQLdb.connect('webmesecure.com', 'adminwms', 'admin@2020', 'devDB')
    return db

# add registered user in register table


def addRegisterToDb(new_register):
    conn = connectToDatabase()
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)

    # Execute the SQL command
    try:
        sql = "INSERT INTO register (phone,email,ipaddress,created) VALUES (%s, %s,%s, %s)"
        val = (new_register['phone'], new_register['email'],
               new_register['ipaddress'], new_register['created'])
        cursor.execute(sql, val)
        conn.commit()
        Registeredusers = showRegistersFromDb()
        for ru in Registeredusers:
            if(new_register['phone'] == ru['phone']):
               return ru
        print(cursor.rowcount, "Registered.")

    except MySQLdb.Error as e:
        print(e)

    finally:
        # disconnect from server
        conn.close()


## show registered user in register table ##

def showRegistersFromDb():
    conn = connectToDatabase()
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)

    # Execute the SQL command
    try:
        sql = "SELECT * FROM register"
        cursor.execute(sql)
        registersList = cursor.fetchall()

        # print(registersList)
        print('registered users list')

        return registersList
    except MySQLdb.Error as e:
        print(e)

    finally:
        # disconnect from server
        conn.close()


## add  user in users table ##


def addUserToDb(new_user):
    conn = connectToDatabase()
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)

    # Execute the SQL command
    try:
        sql = "INSERT INTO users (r_id,name,phone,gender,address,email,dob,usertype,currency,id_photo_path,photo_path,created,updated,active) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
        val = (new_user['r_id'], new_user['name'], new_user['phone'], new_user['gender'],
               new_user['address'], new_user['email'], new_user['dob'], new_user['usertype'],
               new_user['currency'], new_user['id_photo_path'], new_user['photo_path'],
               new_user['created'], new_user['updated'], new_user['active']
               )
        cursor.execute(sql, val)
        conn.commit()
        users = showUsersFromDb()

        for u in users:
            if(u['r_id']==new_user['r_id']):
               return u
        print(cursor.ro, "user added.")

    except MySQLdb.Error as e:
        print(e)

    finally:
        # disconnect from server
        conn.close()


## show  user in users table ##

def showUsersFromDb():
    conn = connectToDatabase()
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)

    # Execute the SQL command
    try:
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        usersList = cursor.fetchall()

        # print(usersList)
        print('users list')

        return usersList
    except MySQLdb.Error as e:
        print(e)

    finally:
        # disconnect from server
        conn.close()
