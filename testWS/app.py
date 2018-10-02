#!flask/bin/python
from flask import Flask,jsonify,current_app
from flask import request
import queries as qs
import json


app = Flask(__name__)


with app.app_context():
    # within this block, current_app points to app.
    print current_app.name


data = qs.getAllUsers()

#create list of user dictionaries
datadict= []
for user in data:
    del user.__dict__['_sa_instance_state']
    #print user.__dict__
    datadict.append(user.__dict__)

#convert dictionary list to json
jsondata=json.dumps(datadict)
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
    print(content['id'])
    print(content['name'])
    return 'JSON posted'

##############################################################
#######################GET ALL################################
##############################################################

@app.route('/getjson', methods=['GET'])
def getAll():
    print(request.is_json)
    print data
    return jsonify({"data": data})

##############################################################
#######################GET ONE################################
##############################################################

@app.route('/getjson/<int:id>', methods=['GET'])
def getById(id):
    for user in data:
        if id == user['id']:
            data_user = user  # type: Dict[str, str]
            print data_user
    return jsonify(data_user)

##############################################################
########################UPDATE################################
##############################################################

@app.route('/updatejson/<int:_id>', methods=['PUT'])
def update(_id):
    update_req = request.json
    for user in data:
        if _id == user['id']:
            index= data.index(user)
            data_user = user
            data_user = update_req
    data[index]= data_user
    return jsonify(data_user)

##############################################################
########################REMOVE################################
##############################################################

@app.route('/removejson/<int:_id>', methods=['DELETE'])
def remove(_id):
    for user in data:
        if _id == user['id']:
            data_user = user
    data.remove(data_user)
    return "user deleted"







app.run(host='0.0.0.0', port=5000)