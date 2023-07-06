#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Artist, Artwork

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")


        print("Seeding artists...")
        artists = [
            Artist(name="Jessie Makinson", medium="painting")
        ]
        db.session.add_all(artists)
        db.session.commit()

        print("Seeding users...")
        users = [
            User(name="John Doe", username="johndoe", role="admin"),
            User(name="Jane Smith", username="janesmith", role="user")
        ]
        db.session.add_all(users)
        db.session.commit()

        print("Seeding artworks...")
        artworks = [
            Artwork(title="we shall be monsters", artist_id=1, medium="painting", image="https://cdn.discordapp.com/attachments/1113536081091108996/1126256462751088640/IMG_5E8598DF9AAC-1.jpeg")
        ]
        db.session.add_all(artworks)
        db.session.commit()

        # print("Seeding collections...")
        # collections = [
        #     Collection(user_id=1, artwork_id=1)
        # ]
        # db.session.add_all(collections)
        # db.session.commit()

        # print("Seed completed successfully!")
        # Seed code goes here!

        # print("Seeding artists...")
        # artists = [
        #     Artist(name="Jessie Makinson", medium="painting")
        # ]
        # db.session.add_all(artists)
        # db.session.commit()

        # print("Seeding artworks...")
        # artworks = [
        #     Artwork(title="we shall be monsters", artist_id=1, medium="painting", image="https://cdn.discordapp.com/attachments/1113536081091108996/1126256462751088640/IMG_5E8598DF9AAC-1.jpeg")
        # ]

        # db.session.add_all(artworks)
        # db.session.commit()

        print("Seed completed successfully!")
