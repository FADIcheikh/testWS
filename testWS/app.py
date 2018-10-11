#!flask/bin/python
from flask import Flask,jsonify,current_app
from flask import request
import json
import Data
from Data import User
from base import session,session2
import redis
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

r = redis.StrictRedis(host='localhost', port=6379, db=0)


with app.app_context():
    # within this block, current_app points to app.
    print current_app.name

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
    session.add(user)
    session.flush()
    session.commit()

    return 'User added'

##############################################################
##################GET ALL+GEt By ID###########################
##############################################################


@app.route('/getjson',defaults={'_id': None}, methods=['GET'])
@app.route('/getjson/<int:_id>', methods=['GET'])
def getAll(_id):
    data = session.query(User).all()
    # create list of user dictionaries
    datadict = []
    for user in data:
        del user.__dict__['_sa_instance_state']
        # print user.__dict__
        datadict.append(user.__dict__)

    # convert dictionary list to json
    print request.args
    jsondata = json.dumps(datadict)
    data_json = json.loads(jsondata)

    if _id == None:
         print "get All"
    else:
        for user in data_json:
            if _id == user['id']:
                data_user = user  # type: Dict[str, str]
                # print data_user
                return jsonify(data_user)
    r.set("data", jsondata)
    return jsondata

##############################################################
#######################GET ONE################################
##############################################################

"""
@app.route('/getjson/<int:id>', methods=['GET'])
def getById(id):
    for user in data_json:
        if id == user['id']:
            data_user = user  # type: Dict[str, str]
            #print data_user
    return jsonify(data_user)"""

##############################################################
########################UPDATE################################
##############################################################


@app.route('/updatejson/<int:_id>', methods=['PUT'])
def update(_id):
    content = request.get_json()
    nom = content['nom']
    email = content['email']
    password = content['password']
    updated_user = Data.User(nom,email,password, kwargs={'id': _id})
    updated_user.id = _id
    session.merge(updated_user)
    session.flush()
    session.commit()

    return "user updated "

##############################################################
########################REMOVE################################
##############################################################


@app.route('/removejson/<int:_id>', methods=['DELETE'])
def remove(_id):
    session2.query(Data.User).filter(User.id == _id).delete()
    session2.commit()
    session2.close()
    session.expire_all()

    return "user deleted"


app.run(host='0.0.0.0', port=5000)