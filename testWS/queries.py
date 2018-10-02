from base import Session
from Data import User

from flask import Flask,jsonify


# 2 - extract a session
session = Session()

# 3 - extract all users
def getAllUsers():
    users = session.query(User).all()
    return users

#test getAllUsers
"""for user in getAllUsers():
    print user.toString()"""

# 3 - extract a user
def getUserByYd(_id):
    user = session.query(User).filter(User.id == _id)
    return user

#test get a user
"""for user in getUserByYd(1):
    print user.toString()"""