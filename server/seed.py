#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Artist, Artwork, Collection

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        # Style.query.delete()
        User.query.delete()
        Artist.query.delete()
        Artwork.query.delete()
        Collection.query.delete()
        print("Starting seed...")
        

        # print("Seeding styles...")
        # styles = [
        #     Style(style_type="Contemporary"),
        #     Style(style_type="Abstract"),
        #     Style(style_type="Minimalist"),
        #     Style(style_type="Landscape"),
        #     Style(style_type="Bold"),
        #     Style(style_type="Sculpture"),
        #     Style(style_type="Surrealism"),
        #     Style(style_type="Impressionism"),
        #     Style(style_type="Pop Art")

        # ]
        # db.session.add_all(styles)
        # db.session.commit()

        print("Seeding artists...")
        artists = [
            Artist(name="Jessie Makinson", medium="painting"),
            Artist(name="Qualeasha Wood", medium="textile"),
            Artist(name="Miranda Forrester", medium="painting"),
            Artist(name="Joana Galego", medium="painting"),
            Artist(name="Alanna Hernandez", medium="colored pencil, painting"),
            Artist(name="Nettle Grellier", medium="oil on canvas"),
            Artist(name="Seline Burn", medium="painting"),
            Artist(name="Natalie Savage", medium="acrylic on canvas"),
            Artist(name="Andie Dinkin", medium="oil on canvas"),
            Artist(name="Daniel Heidkamp", medium="painting"),
            Artist(name="Danielle McKinney", medium="painting"),
            Artist(name="Noah Verrier", medium="painting"),
            Artist(name="Ellen Berkenbilt", medium="painting"),
            Artist(name="Kyle Dunn", medium="acrylic on wood")
        ]
        db.session.add_all(artists)
        db.session.commit()

        print("Seeding users...")
        users = [
            User(name="Sarah Dean", username="letuspray", role="gallerist"),
            User(name="Jan", username="janesmith", role="user")
        ]
        db.session.add_all(users)
        db.session.commit()

        print("Seeding artworks...")
        artworks = [
            Artwork(title="we shall be monsters", artist_id=1, medium="painting", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1126256462751088640/IMG_5E8598DF9AAC-1.jpeg"),
            Artwork(title="Alter Egos/Projected Selves", artist_id=2, medium="textile", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1126909304025399386/1640985483-image-5-qualeasha-woods.webp"),
            Artwork(title="You can lay your hands on me", artist_id=3, medium="painting", style_id=2, image="https://cdn.discordapp.com/attachments/1113536081091108996/1127257306090967100/1650073849-you-can-lay-your-hands-on-me-miranda-forrester.webp"),
            Artwork(title="egocentric with company", artist_id=4, medium="painting", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128462714000380024/IMG_EE27915EE79C-1.jpeg"),
            Artwork(title="The Falling Sky", artist_id=5, medium="colored pencil on wood", style_id=7, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128464073353330829/IMG_4FB6282B24CB-1.jpeg"),
            Artwork(title="Get away with it", artist_id=6, medium="oil on canvas", style_id=4, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128465552273317898/IMG_DD18A2944891-1.jpeg"),
            Artwork(title="The secret garden", artist_id=7, medium="oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128467538917982288/IMG_14F16BF868F2-1.jpeg"),
            Artwork(title="detail", artist_id=7, medium="oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128468405373128734/IMG_41CE698A46C5-1.jpeg"),
            Artwork(title="tapas", artist_id=8, medium="acrylic on canvas", style_id=5, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128469403596496966/IMG_6FE0FE3FCD5E-1.jpeg"),
            Artwork(title="my face for the world to see", artist_id=9, medium="painting", style_id=7, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128471497963475074/IMG_54ACA6E2DC69-1.jpeg"),
            Artwork(title="Chorus", artist_id=10, medium="painting", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128472079801532516/IMG_704D411FB1B3-1.jpeg"),
            Artwork(title="Morning Glory", artist_id=11, medium="painting", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128473376839708702/IMG_52F56975D1A0-1.jpeg"),
            Artwork(title="untitled", artist_id=12, medium="print", style_id=4, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128473889475924070/IMG_07E4D9373890-1.jpeg"),
            Artwork(title="Circa", artist_id=13, medium="painting", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128476093939195984/IMG_BD46ABE633B0-1.jpeg"),
            Artwork(title="Downward Dog", artist_id=14, medium="acrylic on wood", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128477120650301520/IMG_5A69CE0B82F5-1.jpeg"),
            Artwork(title="Night Pictures", artist_id=14, medium="acrylic on wood", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128477791868948571/IMG_CF6B99484656-1.jpeg")
        ]
        db.session.add_all(artworks)
        db.session.commit()


        print("Seeding collections...")
        collections = [
            Collection(user_id=1, artwork_id=1)
        ]
        db.session.add_all(collections)
        db.session.commit()

   

        print("Seed completed successfully!")
