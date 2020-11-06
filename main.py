from flask import Flask, jsonify, request

from database import addUserToDb, showUsersFromDb

# root
app = Flask(__name__)



# home_endPoint
@app.route("/")
def home():
    return "WebMeSecure!"


##Users_endPoint

# listOfUsers_endPoint
@app.route("/users")
def getUsersList():
    users = showUsersFromDb()
    return jsonify(users)


# userbyId_endPoint
@app.route("/users/<string:id>")
def getUser(id):
    users = showUsersFromDb()

    for user in users:
        if(user["id"] == id):
            return user
    return jsonify({'message': 'user not found',
                    'status_code': '404'})


# addUser_endPoint
@app.route("/users", methods=['POST'])
def addUser():
    req_data = request.get_json()
    new_user = {
        'id': req_data['id'],
        "name": req_data['name'],
        "age": req_data['age'],
        "country": req_data['country']
    }
    addUserToDb(new_user)
    return jsonify({'user': new_user,
                    'message': 'user added',
                    'status_code': '200'})

# ##members_endpoint


# # listOfMembers_endPoint
# # @app.route("/members")
# # def getMembersList():
# #     members = showMembersFromDb()
# #     return jsonify(members)


# # membersbyId_endPoint
# @app.route("/members/<string:id>")
# def getUser(id):
#     users = showUsersFromDb()

#     for user in users:
#         if(user["id"] == id):
#             return user
#     return jsonify({'message': 'user not found',
#                     'status_code': '404'})


# # addMembers_endPoint
# @app.route("/members", methods=['POST'])
# def addUser():
#     req_data = request.get_json()
#     new_user = {
#         'id': req_data['id'],
#         "name": req_data['name'],
#         "age": req_data['age'],
#         "country": req_data['country']
#     }
#     addUserToDb(new_user)
#     return jsonify({'user': new_user,
#                     'message': 'user added',
#                     'status_code': '200'})





if __name__ == "__main__":
    app.run(debug=True)
