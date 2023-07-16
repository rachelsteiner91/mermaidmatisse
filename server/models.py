from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin, LoginManager
from sqlalchemy.ext.hybrid import hybrid_property


from config import db, bcrypt

# Models go here!

##USER
class User(db.Model, SerializerMixin, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String)
    created_at = db.Column(db.DateTime)
## USER RELATIONSHIPS
    # collections = db.relationship('Collection', back_populates='user', uselist=False)

    collections = db.relationship('Collection', back_populates='artworks', uselist=False)
    # art_collection = db.relationship('ArtCollection', back_populates='user.id')
##VALIDATIONS
    serialize_rules = ('-collections.artworks',)

    @hybrid_property
    def password_hash(self):
        raise Exception('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))
# #~~~~~~~~~~~~~~~# 
class Artwork(db.Model, SerializerMixin):
    __tablename__ = "artworks"

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    title = db.Column(db.String)
    medium = db.Column(db.String)
    image = db.Column(db.String)
    style_id = db.Column(db.String, db.ForeignKey('styles.id'))
    created_at = db.Column(db.DateTime)
##RELATIONSHIPS    
    artists = db.relationship('Artist', back_populates ='artworks')
    style = db.relationship('Style', backref='artworks') #back referencing itself because it already has a foreign key
##Serializers
    serialize_rules = ("-style_id", "-artists.artworks", "-style.artworks",)
##VALIDATIONS
# #~~~~~~~~~~~~~~~# 
class Collection(db.Model, SerializerMixin):
    __tablename__ = "collections"

    id = db.Column(db.Integer, primary_key=True)
    artwork_id = db.Column(db.Integer, db.ForeignKey('artworks.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime)
##RELATIONSHIPS   
    # user = db.relationship('User', back_populates='collections') 
    artworks = db.relationship('User', back_populates='collections')  
##VALIDATIONS
    serialize_rules = ("-artworks.collections", "-user.collections")
# #~~~~~~~~~~~~~~~# 
class Artist(db.Model, SerializerMixin):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    medium = db.Column(db.String)
    image = db.Column(db.String)
    description = db.Column(db.String)
##RELATIONSHIPS 
    artworks = db.relationship('Artwork', back_populates='artists')

#~~~~~~~~~~~#
class Style(db.Model, SerializerMixin):
    __tablename__ = "styles"

    id = db.Column(db.Integer, primary_key=True)
    style_type = db.Column(db.String, nullable=False)




    # Models go here!

##USER
# class User(db.Model, SerializerMixin):
#     __tablename__ = "users"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     username = db.Column(db.String, nullable=False)
#     role = db.Column(db.String)
#     created_at = db.Column(db.DateTime)
# ## USER RELATIONSHIPS
#     collections = db.relationship('Collection', back_populates='user')
   
# ##VALIDATIONS

# # #~~~~~~~~~~~~~~~# 
# class Artwork(db.Model, SerializerMixin):
#     __tablename__ = "artworks"

#     id = db.Column(db.Integer, primary_key=True)
#     artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
#     title = db.Column(db.String)
#     medium = db.Column(db.String)
#     image = db.Column(db.String)
#     created_at = db.Column(db.DateTime)
# ##RELATIONSHIPS    
#     artist = db.relationship('Artist', back_populates='artworks')
#     collections = db.relationship('Collection', back_populates='artwork')
# ##VALIDATIONS
# # #~~~~~~~~~~~~~~~# 
# class Collection(db.Model, SerializerMixin):
#     __tablename__ = "collections"

#     id = db.Column(db.Integer, primary_key=True)
#     artwork_id = db.Column(db.Integer, db.ForeignKey('artworks.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     created_at = db.Column(db.DateTime)
# ##RELATIONSHIPS    
#     artworks = db.relationship('Artwork', back_populates='collections')  
# ##VALIDATIONS

# # #~~~~~~~~~~~~~~~# 
# class Artist(db.Model, SerializerMixin):
#     __tablename__ = "artists"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     medium = db.Column(db.String)
#     artworks = db.relationship('Artwork', back_populates='artist')

# class ArtCollection(db.Model, SerializerMixin):
#     __tablename__="art_collections"

#     artwork_id = db.Column(db.Integer, db.ForeignKey('artworks.id'), primary_key=True)
#     collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), primary_key=True)


# from sqlalchemy_serializer import SerializerMixin
# from config import db

# # Models go here!

# ##USER
# class User(db.Model, SerializerMixin):
#     __tablename__ = "users"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     username = db.Column(db.String, nullable=False)
#     role = db.Column(db.String)
#     created_at = db.Column(db.DateTime)
    
#     ## USER RELATIONSHIPS
#     collections = db.relationship('Collection', back_populates='user')
#     art_collection = db.relationship('ArtCollection', back_populates='user')

# ##VALIDATIONS

# # #~~~~~~~~~~~~~~~# 
# class Artwork(db.Model, SerializerMixin):
#     __tablename__ = "artworks"

#     id = db.Column(db.Integer, primary_key=True)
#     artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
#     title = db.Column(db.String)
#     medium = db.Column(db.String)
#     image = db.Column(db.String)
#     created_at = db.Column(db.DateTime)
    
#     ##RELATIONSHIPS    
#     artist = db.relationship('Artist', back_populates='artworks')
#     collections = db.relationship('Collection', back_populates='artwork')

# ##VALIDATIONS

# # #~~~~~~~~~~~~~~~# 
# class Collection(db.Model, SerializerMixin):
#     __tablename__ = "collections"

#     id = db.Column(db.Integer, primary_key=True)
#     artwork_id = db.Column(db.Integer, db.ForeignKey('artworks.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     created_at = db.Column(db.DateTime)
    
#     ##RELATIONSHIPS    
#     artwork = db.relationship('Artwork', back_populates='collections')  

# ##VALIDATIONS

# # #~~~~~~~~~~~~~~~# 
# class Artist(db.Model, SerializerMixin):
#     __tablename__ = "artists"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     medium = db.Column(db.String)
    
#     artworks = db.relationship('Artwork', back_populates='artist')



