from flask import Flask, jsonify, request

from database import addRegisterToDb, showRegistersFromDb, addUserToDb, showUsersFromDb


# root
thisAppVar = Flask(__name__)

# home_endPoint
@thisAppVar.route("/")
def home():
    return "WebMeSecure!"


# registers_endPoint

# listOfRegisters_endPoint
@thisAppVar.route("/registers")
def getRegistersList():
    registers = showRegistersFromDb()
    return jsonify(registers)


# userbyId_endPoint
@thisAppVar.route("/registers/<int:id>")
def getRegister(id):
    registers = showRegistersFromDb()

    for register in registers:
        if(register["r_id"] == id):
            return register
    return jsonify({'message': 'user not found',
                    'status_code': '404'})


# addRegister_endPoint
@thisAppVar.route("/registers", methods=['POST'])
def addRegister():
    req_data = request.json
    new_register = {
        'phone': req_data['phone'],
        'email': req_data['email'],
        "ipaddress": req_data['ipaddress'],
        "created": req_data['created']
    }
    added_user= addRegisterToDb(new_register)

    return jsonify({'registerUser': added_user,
                    'message': 'user registered',
                    'status_code': '200'})






#############users EndPoints  #######################


# listOfUsers_endPoint
@thisAppVar.route("/users")
def getUsersList():
    users = showUsersFromDb()
    print(users)
    return jsonify(users)


# userbyId_endPoint
@thisAppVar.route("/users/<int:id>")
def getUser(id):
    users = showUsersFromDb()

    for user in users:
        if(user["r_id"] == id):
            return user
    return jsonify({'message': 'user not found',
                    'status_code': '404'})


# adduser_endPoint
@thisAppVar.route("/users", methods=['POST'])
def addUser():
    req_data = request.json
    new_user = {
        'r_id': req_data['r_id'],
        'name': req_data['name'],
        'phone': req_data['phone'],
        'gender': req_data['gender'],
        'address': req_data['address'],
        'email': req_data['email'],
        'dob': req_data['dob'],
        'usertype': req_data['usertype'],
        'currency': req_data['address'],
        'id_photo_path': req_data['id_photo_path'],
        'photo_path': req_data['photo_path'],
        'created': req_data['created'],
        'updated': req_data['updated'],
        'active': req_data['active']
    }
    print('aaaaaa')
    addedUser= addUserToDb(new_user)
    print('cccccc')
    return jsonify({'user': addedUser,
                    'message': 'user added',
                    'status_code': '200'})


if __name__ == "__main__":
    thisAppVar.run(debug=True)
