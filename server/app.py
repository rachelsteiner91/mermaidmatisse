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
   






if __name__ == '__main__':
    app.run(port=5555, debug=True)
