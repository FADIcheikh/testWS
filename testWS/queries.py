from base import Session
from Data import User
from sqlalchemy import update

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

# 4 - extract a user
def getUserByYd(_id):
    user = session.query(User).filter(User.id == _id)
    return user

#test get a user
"""for user in getUserByYd(1):
    print user.toString()"""

# 5 - update a user
def updateUser(_id,user):
    user = session.query(User).filter(User.id == _id).update(user)
    session.commit()

#updateUser(5)

# 6 - remove a user
def removeUser(user):
    session.delete(user)
    session.commit()


# 6 - add a user
def addUser(user):
    session.add(user)
    session.commit()

