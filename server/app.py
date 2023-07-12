#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource
from flask_migrate import Migrate
from flask import Flask, request, session, make_response, jsonify, redirect

# Local imports
from config import app, db, api 
from models import db, User, Artist, Collection, Artwork, Style

migrate = Migrate(app, db)
# Views go here!
@app.route("/")
# @cross_origin()
def howdy():
  return "Howdy partner!"


#~~~~~~~Artworks~~~~~~~~~#

# GET/artworks -- need to add ##only to get
class Artworks(Resource):
   def get(self):
      artworks = Artwork.query.all()
      artworks_dict = [a.to_dict(only=('id', 'title', 'medium',  'artists.name', 'style.style_type', 'image')) for a in artworks]
      res = make_response(
         artworks_dict,
         200
      )
      return res
api.add_resource(Artworks, '/artworks')
#GET/ artworks/<int:id>
class OneArtwork(Resource):
   def get(self, id):
        artwork = Artwork.query.filter_by(id=id).first()
        if not artwork:
            return {"404": "Artwork Not Found"}, 404
        
        res = make_response(
            artwork.to_dict(only=('id', 'title', 'medium', 'image', 'artists.name', 'style.style_type')),
            200
        )
        return res
api.add_resource(OneArtwork, "/artworks/<int:id>")
#~~~~~~~Styles~~~~~~~~~#

#GET / styles
class Styles(Resource):
   def get(self):
      styles = Style.query.all()
      styles_dict = [s.to_dict() for s in styles]
      res = make_response(
         styles_dict,
         200
      )
      return res
api.add_resource(Styles, '/styles')
#GET /styles/<int:id>
class OneStyle(Resource):
   def get(self, id):
        style = Style.query.filter_by(id=id).first()
        if not style:
            return {"404": "Style Not Found"}, 404
        
        res = make_response(
            style.to_dict(only=('id', 'style_type')),
            200
        )
        return res
api.add_resource(OneStyle, "/styles/<int:id>")



#~~~~~~~~Artists~~~~~~~~#
class Artists(Resource):
   def get(self):
      artists = Artist.query.all()
      artists_dict = [a.to_dict(only=('id', 'name', 'medium', 'artworks.title', 'artworks.image')) for a in artists]
      res = make_response(
         artists_dict,
         200
      )
      return res
api.add_resource(Artists, '/artists')
#GET/ artworks/<int:id>
class OneArtist(Resource):
   def get(self, id):
        artist = Artist.query.filter_by(id=id).first()
        if not artist:
            return {"404": "Artist Not Found"}, 404
        
        res = make_response(
            artist.to_dict(only=('id', 'name', 'medium', 'artworks.title', 'artworks.image')),
            200
        )
        return res
   
api.add_resource(OneArtist, "/artists/<int:id>")




#~~~~~~~Collections~~~~~~~~~#
class NewCollection(Resource):
    def get(self):
        collections = Collection.query.all()
        collections_dict = [c.to_dict(only = ("id","artwork_id", "user_id")) for c in collections]
        return make_response(collections_dict, 200)
    def post(self):
        data=request.get_json()
       
        try:
            new_collection = Collection(
                artwork_id = data.get('artwork_id'),
                user_id = data.get('user_id')
            )
            db.session.add(new_collection)
            db.session.commit()
        except:
            return make_response({"ERROR"}, 422)
        
        return make_response(new_collection.to_dict(), 201)
api.add_resource(NewCollection, '/collections')
class UserCollection(Resource):
    def get(self, id):
        one_collection = Collection.query.filter_by(id=id).first()
        if not one_collection:
            return {"404": "Collection not found"}, 404
        
        return make_response(
            one_collection.to_dict(only=('id', 'artwork_id', 'user_id')),
            200
        )
        
    def patch(self,id):
        collection = Collection.query.filter_by(id=id).first()
        if not collection:
            return ({'error': '404: collection not found'}, 404)
        try:
            data=request.get_json()
            for attr in data:
                setattr(collection, attr, data.get(attr))
            db.session.add(collection)
            db.session.commit()
            return make_response(collection.to_dict(only=('collection',)),202)
        except:
            return {'error': '400'}
api.add_resource(UserCollection, "/collections/<int:id>")




#~~~~~~~Signup~~~~~~~#
class Signup(Resource):
   def post(self):
      data = request.get_json()
      new_user = User(
         name = data.get('name'),
         username = data.get('username'),
         role = data.get('role')
      )
      db.session.add(new_user)
      db.session.commit()
      session['user_id'] = new_user.id
      return make_response(new_user.to_dict(), 201)
api.add_resource(Signup, '/signup')
#~~~~~~Login~~~~~~~#
# class Login(Resource):
#     def post(self):
#         data = request.get_json()
#         user = User.query.filter_by(username = data.get('username')).first()


#~~~~~~~~~~~~#
#AUTH#
class AuthorizedSession(Resource):
    def get(self):
        try:
            user = User.query.filter_by(
                id = session.get('user_id')).first()
            return make_response(user.to_dict(), 200)
        except:
            return make_response({'message': 'Must log in'}, 401)
api.add_resource(AuthorizedSession, '/authorize_session')

#~~~~~~~Users~~~~~~~~~#

class Users(Resource):
   def get(self):
      users = User.query.all()
      users_dict = [u.to_dict(only=('id', 'name', 'username', 'role')) for u in users]
      res = make_response(
         users_dict,
         200
      )
      return res
   
api.add_resource(Users, '/users')
class CurrentUser(Resource):
   def get(self, username):
      user = User.query.filter(User.username == username).first()
      if not user:
            return make_response("User not found", 404)
      return make_response(user.to_dict(), 200)
api.add_resource(CurrentUser, '/users/<string:username>')






   






if __name__ == '__main__':
    app.run(port=5555, debug=True)
