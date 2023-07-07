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
      artworks_dict = [a.to_dict() for a in artworks]
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
            artwork.to_dict(only=('id', 'title', 'medium', 'image', 'artist_id')),
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





#~~~~~~~Collections~~~~~~~~~#






#~~~~~~~Users~~~~~~~~~#
class Users(Resource):
   def get(self):
      users = User.query.all()
      users_dict = [u.to_dict() for u in users]
      res = make_response(
         users_dict,
         200
      )
      return res
   
api.add_resource(Users, '/users')



   






if __name__ == '__main__':
    app.run(port=5555, debug=True)
