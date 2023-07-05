#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import User, Artist, ArtCollection, Collection, Artwork

# Views go here!
@app.route("/")
# @cross_origin()
def howdy():
  return "Howdy partner!"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
