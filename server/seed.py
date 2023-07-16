#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Artist, Artwork, Collection

def clear_tables():
    db.session.query(User).delete()
    db.session.commit()


if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        clear_tables()
        # Style.query.delete()
        # User.query.delete()
        Artist.query.delete()
        Artwork.query.delete()
        # Collection.query.delete()
        # print("Starting seed...")
        

        # # print("Seeding styles...")
        # # styles = [
        # #     Style(style_type="Contemporary"),
        # #     Style(style_type="Abstract"),
        # #     Style(style_type="Minimalist"),
        # #     Style(style_type="Landscape"),
        # #     Style(style_type="Bold"),
        # #     Style(style_type="Sculpture"),
        # #     Style(style_type="Surrealism"),
        # #     Style(style_type="Impressionism"),
        # #     Style(style_type="Pop Art")

        # # ]
        # # db.session.add_all(styles)
        # # db.session.commit()

        print("Seeding artists...")
        artists = [
            Artist(name="Jessie Makinson", medium="painting", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130183841072549999/1560x0.webp", description="Jessie Makinson's work is darkly erotic and draws from influences including Ursula Le Guin, British folklore, stories of travelers, myths of pre-agricultural societies, 17th and 18th-century erotica, Flemish kitchen scenes, science fiction, and early Renaissance altarpieces. Makinson readdresses a patriarchal past from a female perspective. Plucking themes and narratives from historical precedent, she creates a bold new context for the motifs she selects. Vivid colors describe tense, erotic scenes in which women are dangerous active participants, not passive permission givers. Makinson’s characters practice rituals, they embrace, plot, and conspire. They hold sexual power and disrupt expectations, inhabiting a universe that surprises, delights, and tests its audience. Jessie Makinson (b. 1985, London, UK) lives and works in London."),
            Artist(name="Qualeasha Wood", medium="textile", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130193865824014497/qw.jpg", description="At RISD, she began to regret her career intentions. “I went to school to illustrate [children’s books] because I was taught that to be a Black artist, I had to do something useful with it,” she explains, “[But] halfway through my freshman year, I literally hated drawing. It became the thing of my nightmares.” When her professor called with an excuse to get out of class, Wood jumped at it. Little did she know, she’d be sharing a limo ride with Tar Beach author Faith Ringgold, and her future would be radically altered. “Her work is all quilts. It’s all textiles and is narrative-based,” Wood says. “So every single piece tells us a story, and that made sense to me.” Wood told Ringgold about her desire to switch mediums, more inspired by her grandmother's quilts than by traditional art history, to which Ringgold responded: “Go do whatever you want because other people don't have the option to.” Then they took a selfie. Wood changed her major the next day. https://www.wmagazine.com/culture/qualeasha-wood-artist-interview-met-museum-hauser-wirth-2022"),
            Artist(name="Miranda Forrester", medium="painting", image="", description=""),
            Artist(name="Joana Galego", medium="painting", image="", description=""),
            Artist(name="Alanna Hernandez", medium="colored pencil, painting", image="", description=""),
            Artist(name="Nettle Grellier", medium="oil on canvas", image="", description=""),
            Artist(name="Seline Burn", medium="painting", image="", description=""),
            Artist(name="Natalie Savage", medium="acrylic on canvas", image="", description=""),
            Artist(name="Andie Dinkin", medium="oil on canvas", image="", description=""),
            Artist(name="Daniel Heidkamp", medium="painting", image="", description=""),
            Artist(name="Danielle McKinney", medium="painting", image="", description=""),
            Artist(name="Noah Verrier", medium="painting", image="", description=""),
            Artist(name="Ellen Berkenbilt", medium="painting", image="", description=""),
            Artist(name="Kyle Dunn", medium="acrylic on wood", image="", description=""),
            Artist(name="Dominic Chambers", medium="painting", image="", description=""),
            Artist(name="Sophia Heymans", medium="multimedia", image="", description=""),
            Artist(name="Ana Benaroya", medium="painting", image="", description=""),
            Artist(name="Laure Mary Couegnias", medium="oil on canvas", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130190532862279862/C9s_nyAWsAY-O42.jpg", description=""),
            Artist(name="Quentin James McCaffrey", medium="oil on canvas, panel", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130189758677651607/img_4150.webp", description="McCaffrey’s worlds are of an arrested time, a stillness emphasizing the activity that is outside its borders. Using single-point perspective, layers of oil paint on panel or canvas, and a focus on light, he renders domestic interior spaces. His motionless interiors seek to call into question the narratives that become ingrained in one’s understanding of the world.McCaffrey’s paintings draw from Quattrocento Italian painting and 17th century Dutch interiors in their use of simple geometry, symbolism, as well as in their stoicism. In western painting, the domestic interior has been a place for investigating the psyche and intimate relationships. Referencing the nostalgia of 19th century academic painting, his paintings allow a space for questioning the forgetful serenity often depicted and acknowledges an undercurrent of a more complex reality. Drawing a parallel between intimate personal experience and imperfect historic narratives, he compares the domestic and psychological interior, and how they are mutually symbolic and influential.")




        ]
        db.session.add_all(artists)
        db.session.commit()

        # print("Seeding users...")
        # users = [
        #     User(name="Sarah Dean", username="letuspray", role="gallerist"),
        #     User(name="Jan", username="janesmith", role="user")
        # ]
        # db.session.add_all(users)
        # db.session.commit()

        print("Seeding artworks...")
        artworks = [
            Artwork(title="we shall be monsters", artist_id=1, medium="painting", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1126256462751088640/IMG_5E8598DF9AAC-1.jpeg"),
            Artwork(title="FOREVA' By Cardi B", artist_id=2, medium="textile", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1126909304025399386/1640985483-image-5-qualeasha-woods.webp"),
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
            Artwork(title="Night Pictures", artist_id=14, medium="acrylic on wood", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128477791868948571/IMG_CF6B99484656-1.jpeg"),
            Artwork(title="Courts (meditation in black)", artist_id=15, medium="oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128485218047754240/IMG_C59F46881C3F-1.jpeg"),
            Artwork(title="Fallen Daughters", artist_id=16, medium="papier mache, molding paste, multimedia, oil on canvas", style_id=2, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128484369405837453/IMG_CF8BDFADF28E-1.jpeg"),
            Artwork(title="A Full Moon", artist_id=17, medium="painting", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128697183076614246/AnaBenaroya_AFullMoon.jpg"),
            Artwork(title="By The Ocean's Roar", artist_id=17, medium="painting", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128698800219881552/ABENA015_001.jpg"),
            Artwork(title="Everything but...", artist_id=18, medium="painting, oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1129854458461958235/image.png"),
            Artwork(title="The Time of the Beginning", artist_id=18, medium="painting, oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1129855275822756000/image.png"),
            Artwork(title="Hour of light", artist_id=19, medium="oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1129876930401947810/image.png")
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
