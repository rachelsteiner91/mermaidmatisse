from sqlalchemy_serializer import SerializerMixin


from config import db

# Models go here!

##USER
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    role = db.Column(db.String)
    created_at = db.Column(db.DateTime)
## USER RELATIONSHIPS
    collections = db.relationship('Collection', back_populates='user.id')
    art_collection = db.relationship('ArtCollection', back_populates='user.id')
##VALIDATIONS

# #~~~~~~~~~~~~~~~# 
class Artwork(db.Model, SerializerMixin):
    __tablename__ = "artworks"

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    title = db.Column(db.String)
    medium = db.Column(db.String)
    created_at = db.Column(db.DateTime)
##RELATIONSHIPS    

##VALIDATIONS
# #~~~~~~~~~~~~~~~# 
class Collection(db.Model, SerializerMixin):
    __tablename__ = "collections"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime)
##RELATIONSHIPS    
    artworks = db.relationship('Artwork', back_populates='collections')  
##VALIDATIONS

# #~~~~~~~~~~~~~~~# 
class Artist(db.Model, SerializerMixin):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    medium = db.Column(db.String)
    artworks = db.relationship('Artwork', back_populates='artists')

class ArtCollection(db.Model, SerializerMixin):
    __tablename__="art_collections"

    artwork_id = db.Column(db.Integer, db.ForeignKey('artworks.id'), primary_key=True)
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), primary_key=True)