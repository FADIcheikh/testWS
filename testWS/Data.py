from sqlalchemy import Column, String, Integer, Date
from base import Base
import  json


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    email = Column(Date)
    password = Column(String)

    def __init__(self, email,password):
        self.email = email
        self.password = password

    def toString(self):
        return  "user: "+self.nom + " email : "+self.email

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)