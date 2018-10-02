from sqlalchemy import Column, String, Integer, Date
from base import Base
import  json


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    email = Column(Date)
    password = Column(String)

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email


    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def __init__(self, id, nom,email,password):
        self.id = id
        self.nom = nom
        self.email = email
        self.password = password


    def toString(self):
        return  "user: "+self.nom + " email : "+self.email

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    def getUserById(self,_id):
        if self.id == _id:
            return self
