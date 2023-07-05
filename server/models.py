from sqlalchemy_serializer import SerializerMixin

from config import db

# Models go here!

#Curator
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True)

##RELATIONSHIPS

##VALIDATIONS
