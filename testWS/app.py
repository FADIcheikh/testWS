#!flask/bin/python
from flask import Flask,jsonify,current_app
from flask import request
import json
import Data
from Data import User
from base import session,session2


app = Flask(__name__)


with app.app_context():
    # within this block, current_app points to app.
    print current_app.name



data =  session.query(User).all()
print data
#create list of user dictionaries
datadict= []
for user in data:
    del user.__dict__['_sa_instance_state']
    #print user.__dict__
    datadict.append(user.__dict__)

#convert dictionary list to json
jsondata=json.dumps(datadict)
data_json = json.loads(jsondata)
print "objects serialized: " + jsondata


"""
data = [{
    "id": 22,
    "name": "fadi"
},
    {
    "id": 20,
    "name": "xxx"
    }]
"""


##############################################################
#########################POST#################################
##############################################################

@app.route('/postjson', methods=['POST'])
def post():
    print(request.is_json)
    content = request.get_json()
    nom = content['nom']
    email = content['email']
    password = content['password']
    user = Data.User(nom,email,password)
    #print user.toString()
    session.add(user)
    session.commit()
    return 'JSON posted'

##############################################################
#######################GET ALL################################
##############################################################

@app.route('/getjson', methods=['GET'])
def getAll():
    print(request.is_json)
    #print data
    return jsonify({"data": jsondata})

##############################################################
#######################GET ONE################################
##############################################################

@app.route('/getjson/<int:id>', methods=['GET'])
def getById(id):
    for user in data_json:
        if id == user['id']:
            data_user = user  # type: Dict[str, str]
            #print data_user
    return jsonify(data_user)

##############################################################
########################UPDATE################################
##############################################################

@app.route('/updatejson/<int:_id>', methods=['PUT'])
def update(_id):
    #update_req = request.json
    content = request.get_json()
    nom = content['nom']
    email = content['email']
    password = content['password']
    updated_user = Data.User(nom,email,password, kwargs={'id': _id})
    updated_user.id = _id

    for user in data:
        if _id == user.id:
            #index= data.index(user)
            user = updated_user
            session.merge(user)
            session.flush()
            session.commit()
    return "user updated "

##############################################################
########################REMOVE################################
##############################################################

@app.route('/removejson/<int:_id>', methods=['DELETE'])
def remove(_id):
    session2.query(Data.User).filter(User.id ==_id).delete()
    session2.commit()


    """
    for user_x in data:
        if _id == user_x.id:
            index= data.index(user)
            #user_x = user_to_delete
            user_x = data[index]
    del data[index]
    print user_x
    session.flush()
    session.commit()
    session.expire_all()"""




    return "user deleted"


app.run(host='0.0.0.0', port=5000)