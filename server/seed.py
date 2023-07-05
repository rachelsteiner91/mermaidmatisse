#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        # print("Seeding artists...")
        # artists = [
        #     Artist(name="Jessie Makinson", medium="painting")
        # ]
        # db.session.add_all(artists)

        # print("Seeding artworks...")
        # artworks = [
        #     Artwork(title="we shall be monsters", artist_id=1, medium="painting", image="https://cdn.discordapp.com/attachments/1113536081091108996/1126256462751088640/IMG_5E8598DF9AAC-1.jpeg")
        # ]

        # db.session.add_all(artworks)
