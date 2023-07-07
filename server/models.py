from sqlalchemy_serializer import SerializerMixin


from config import db


#~~~~~~~~~~~~~~~#
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
    collections = db.relationship('Collection', back_populates='artworks')
    # art_collection = db.relationship('ArtCollection', back_populates='user.id')
##VALIDATIONS
    serialize_rules = ('-collections.artworks',)
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
    artworks = db.relationship('User', back_populates='collections')  
##VALIDATIONS

# #~~~~~~~~~~~~~~~# 
class Artist(db.Model, SerializerMixin):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    medium = db.Column(db.String)
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



