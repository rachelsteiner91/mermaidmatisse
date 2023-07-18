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
            Artist(name="Qualeasha Wood", medium="textile", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130193865824014497/qw.jpg", description="At RISD, she began to regret her career intentions. “I went to school to illustrate [children’s books] because I was taught that to be a Black artist, I had to do something useful with it,” she explains, “[But] halfway through my freshman year, I literally hated drawing. It became the thing of my nightmares.” When her professor called with an excuse to get out of class, Wood jumped at it. Little did she know, she’d be sharing a limo ride with Tar Beach author Faith Ringgold, and her future would be radically altered. “Her work is all quilts. It’s all textiles and is narrative-based,” Wood says. “So every single piece tells us a story, and that made sense to me.” Wood told Ringgold about her desire to switch mediums, more inspired by her grandmother's quilts than by traditional art history, to which Ringgold responded: “Go do whatever you want because other people don't have the option to.” Then they took a selfie. Wood changed her major the next day."),
            Artist(name="Miranda Forrester", medium="oil and gloss", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130885666616651856/miranda_forrester.png", description="Miranda Forrester is a figurative painter living and working in London. Forrester explores the queer Black female gaze in painting vis a vis the history of men painting womxn naked. Her work addresses the invisibility of Black womxn in the western history of art. She investigates how painting is able to re-articulate the language and history of life drawing through a queer Black feminist and desiring lens. In doing so, she depicts what the male gaze may not be able to see. Her use of stretching plastic over stretchers and painting on highly primed smooth surfaces is fundamental to the work, as it allows the viewer to see through the pictured bodies; the surface becomes more than skin, allowing the figures to become real and alive, moving and breathing on the canvas. This layering of transparent materials alludes to the complexities and nuances of womanhood and femininity; gender and sexuality."),
            Artist(name="Joana Galego", medium="painting", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130886712189526036/Joana-Galego-studio-portrait-Oliver-Projects-crop.jpg", description="Joana Galego was born in 1994 between not so tall mountains and the Atlantic Ocean, in Cascais, Portugal. After studying Painting at the University of Lisbon she moved to London for The Drawing Year, determined to stop working from photographs of her childhood. She is interested in language, love - in its many forms or absences - and one’s simultaneous hesitancy and excitement. Fascinated by drawing’s affair with failure she now works from memories, observational studies and yes, old photographs."),
            Artist(name="Alanna Hernandez", medium="colored pencil, painting", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130887490283249774/Studio6.webp", description="Alanna Hernandez (b. 1988) grew up on Cape Cod, and graduated from the University of Massachusetts Amherst in 2010, where she earned a B.A. in Middle East Studies. During this time she gained some formal art training, as well as education in art history, history, and language. After graduating, she continued her art practice while training in yoga and meditation. Her work is a culmination of this combination of formal education in the arts and humanities, training in yoga and meditation, and self-taught art skills. She moved to Midcoast Maine in 2018 and currently resides in Union, Maine. Alanna creates abstract work about trauma and human relationships. She is interested in how trauma is felt in our bodies, how it interrupts our lives, and how it ripples down through communities and generations. She uses abstract ribbon forms that are interrupted by external objects to explore these ideas. Her composition uses movement, and tension to create visual flow and focal points. These drawings are created with layers of crosshatched colored pencil and wax pastel. The process is meditative and the overall effect is serene, contrasting with the difficult metaphorical themes of the work."),
            Artist(name="Nettle Grellier", medium="oil on canvas", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130888389764317254/delphian-gallery-Nettle-grellier-podcast-header.jpg", description="Nettle Grellier (b. 1993, Stroud, England) graduated with a BA in Fine Art Painting from the University of Brighton in 2015, before completing the Turps Banana Correspondence Course in 2020. Nettle's work considers the figure through several semi-autobiographical motifs: disobedient dogs, soft bodies, and disquieting, gossipping subjects. Taking influences from artists such as Paula Rego and Dolly Parton, she uses references across high and low culture to delight in unashamedly slovenly, feral, and unpredictable womanhood. Based in Cornwall, and having always lived and worked in rural settings, Nettle also examines the nature of gossip and storytelling as tradition."),
            Artist(name="Seline Burn", medium="painting", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130889316432879646/SelineBurn-2022-1.jpg", description="Seline Burn (b. 1995) is an artist based in Basel, Switzerland. Her painting, which draws influences from symbolism, conjures evocative images where intimacy and radical strangeness are delicately balanced in a practice that she understands as an on-going personal diary. The figures depicted are often in a dreamy, introverted state and seem sleepy or turned away from their surrounding. This way of exploring inner worlds is reminiscent of the symbolic painting of the 19th century, here brought to the present by the garish color palette of the artist, and points to the presence of ancestral myths."),
            Artist(name="Natalie Savage", medium="acrylic on canvas", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130889730557481031/IMG_9662-scaled.jpg", description="Bold and bright colour is heavily important to the aesthetic of Natalie’s work as well as imagery reflecting on today’s pop culture. Both David Hockney and Henri Matisse’s style of painting and use of colour has been heavily influential to Natalie’s work. After receiving a BA (Hons) in Fine Art in Bristol, Natalie went to Central America where the strong colours and simple styles featured in Mexican and Guatemalan art became something Natalie draws huge inspiration from as well as a plethora of sources in everyday life; from flea markets to fashion magazines where unique pieces can be found to be included in paintings"),
            Artist(name="Andie Dinkin", medium="oil on canvas", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130890366996992061/selfportrait.jpg", description="Andie Dinkin graduated with a BFA honors from Rhode Island School of Design in 2014. She is currently working in Los Angeles as a freelance artist. Collectors Include: The Lucas Museum of Narrative Art, University of Maine Museum, The New Yorker, Gigi’s Hollywood, DDG Partners, Studio Shamshiri, Project: ARTSpace, Stein Eriksen Residences, Vincenti Brentwood, Regent Properties, The Standish, Brooklyn "),
            Artist(name="Daniel Heidkamp", medium="painting", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130890556554362930/h1yuK-W3lQS3ZBiHztJs7A_2015-07-07_12-13-17.jpg", description="“In the studio, I’m focused a lot on creating illusionistic light,” he explains. “A lot of that is just based on getting the right color vibrations, really subtle shifts in color to make it appear like light.” His standby methods were hard to execute with the new materials. “We got it to work sometimes, but I gave up that emphasis a little bit. I love looking at Alex Katz and Fairfield Porter, and those guys who are great at making light. And in here, I shifted more to looking at Gauguin, where you still feel that atmosphere and that energy but it’s less about illusionistic light; it’s more about different bright colors coming up against each other."),
            Artist(name="Danielle McKinney", medium="painting", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130893775716220981/DMC_Portrait_Pierre-Le-Hors.webp", description="Danielle Mckinney (b. 1981, Montgomery, Alabama) creates narrative paintings that often focus on the solitary female protagonist. In these intimate portraits, Mckinney captures the figure immersed in various leisurely pursuits and moments of deep reflection. Engaging with themes of spirituality and self, her paintings uncover hidden narratives and conjure dreamlike spaces, often within the interior domestic sphere. With a background in photography, Mckinney paints with an acute awareness of the female gaze, employing deeply colorful hues and nuanced details with cinematic effect.Danielle Mckinney completed her BFA at Atlanta College of Arts in 2005 and her MFA at Parsons School of Design in 2013. Her work is in private and public collections including the Hirshhorn Museum and Sculpture Garden, Washington DC; Dallas Museum of Art, Dallas, TX; Institute of Contemporary Art, Miami, FL; The Israel Museum, Jerusalem, Israel; and the Hessel Foundation Collection at Bard, Annandale-on-Hudson, NY. Her work has been included in the exhibitions Heroic Bodies at the Rudolph Tegners Museum, Dronningmølle, Denmark, IN A DREAM YOU SAW A WAY TO SURVIVE AND YOU WERE FULL OF JOY at The Contemporary Austin, Uncanny Interiors at Nicola Vassel Gallery, and Black Melancholia at Hessel Museum of Art. She is represented by Marianne Boesky Gallery in New York and Night Gallery in Los Angeles. Mckinney lives and works in Jersey City, NJ."),
            Artist(name="Noah Verrier", medium="painting", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130894851777511444/pg_99341391461749.jpg", description="Noah Verrier is a former Art Professor and full time working Artist. Noah holds a BFA and MFA (highest attainable degree for a working Artist) specializing in oil painting. Verrier’s work has been exhibited around the world including in (Japan, Australia, Germany, India, Canada, the UK and France) and has been collected by thousands including celebrities such as William Tomicki the former Vice President of Sotheby’s and Tiffany. And Commissioned by Popeyes, Little Caesars, Quick Trip Gas Stations, (Chris Cantino) for Club CPG's POP collection. Noah has garnered numerous awards for his paintings including “One of the top 40 American Painters” by New American Paintings. Verrier’s work has been featured by many well known online and print publications including Bonappetit, Yahoo News, Buzzfeed, International Artist's Magazine, Narcity, WGN Morning News and in Entree Magazine where Noah’s work was called “Masterful and painterly, reminiscent of still life greats like Chardin, Sargent and Manet”. Noah lives and works in Tallahassee, FL happily married with his wife four kids a cat and a dog."),
            Artist(name="Ellen Berkenblit", medium="painting", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130893100278095982/9fd2436904a71f4de245922ea611c5d6.jpg", description="For more than 30 years, Ellen Berkenblit has been exploring line in her large-scale, exuberant paintings, combining an Abstract Expressionistic style with comic strip characters of her own invention. Though the recurring figure of a young girl and her animal consorts suggest narratives, Berkenblit sees these figures as collections of lines, devices that organize and drive her overall composition. As she explains: “The figures I choose have one purpose: they carry the line that I wish to draw. The figures are not symbolic; they don't represent anyone or anything in particular. They are the perfect excuse to get the first line going.” In Tigers vs Witches (2013), the profiles of a tiger and a witch face each other across the canvas. Their kinetic lines lead the eye to the deftly composed abstract shapes and colors filling and animating the work."),
            Artist(name="Kyle Dunn", medium="acrylic on wood", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130892905247162421/c5ceeb59604958a37b021dd5d6d9e0c0.jpg", description="Kyle Dunn’s Night Pictures offers quiet, intimate scenes that hum with depth. In one painting, A Night Off (2023), a couple lie together in bed, the tops of their heads visible as one turns toward the other while he looks at the ceiling; they are bathed in rose-colored light, the sheets are mussed, and the glimpse of outside through the window suggests early evening. The lower half of the canvas shows a dog asleep under the bed, an abandoned cocktail, a box of matches, a bowl, and fruit. In other words, this is queer life that lingers in the afterglow or aftermath—what happens after the party, after sex? Under the rubric of domesticity—cocktails, dogs, and fashionable garments—the show brings together a wealth of ambivalent emotions, seemingly brought about by the day’s slide into night. Does queer domesticity evoke calm or claustrophobia? The faces of his subjects are often turned away from the viewer—absorbed in their evening thoughts and tasks, so that their emotional responses are unreadable. The psychological qualities of “night” also vary; Dunn presents “afters” in the form of coming home, getting undressed, stretching as well as moments “before” with subjects in contemplation, studying a relatively blank canvas, or journaling. Are these scenes of exhausted dénouement or anxious anticipation? There is a more profound message behind this ambiguity; these paintings are also about the complexity and unknowability of interiority itself. One way that we see this is in Dunn’s use of mirrors and windows, both of which bring the outside into these domestic scenes, signaling a collapse between the physical boundaries between interior and exterior. We can also trace the impact of this porosity of the interior in the ways that Dunn incorporates himself, his personal life, and cultural and historical referents into the people in his paintings, who are described as composites. These conjunctions make the paintings into ciphers, setting the viewer up to question what they are seeing and what they are projecting."),
            Artist(name="Dominic Chambers", medium="painting", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130891475031437383/6507ef6f-8938-4bb7-873a-5df70cb2e09a.jpg", description="Drawing loosely upon a tradition of contemporary mystical realism, Dominic Chambers (b. 1993, St. Louis, MO; based in New Haven, CT) creates paintings that immediately reference literary narratives cited in books, various mythologies and Black history, both in its oral tradition and written account. His current practice is invested in exploring Black introspection, the Black body, and the construction of lived Black experiences, as seen through moments of quiet contemplation and meditation, reading, leisure, and camaraderie between friends. An avid reader since childhood, literature and the dialectics of language continues to play a major role in both his life and work. In his psychological figurative paintings, Chambers builds a relationship between history, painting, and the imagination to center his respective ideas of where and how to find joy through respite, one that is both real and longed for. Chambers received his BFA from the Milwaukee Institute of Art and Design in 2016 and later, his MFA from the Yale University School of Art in 2019, where he studied painting. He has exhibited both in The United States and internationally, including Philbrook Museum of Art, Tulsa, OK; MIAD Contemporary Gallery, Milwaukee, WI; and the August Wilson African American Cultural Center, Pittsburgh, PA. He has also participated in a number of residencies including the prestigious Yale Norfolk Summer residency in New Haven, CT and the New York Studio Residency Program in Brooklyn, NY."),
            Artist(name="Sophia Heymans", medium="multimedia", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130896223629484134/e4592ae3e2c609e729e0304e15aefec6.jpg", description="Sophia Heymans’ landscape paintings explore the relationship between the land and humankind, playing on viewers' natural inclination to see themselves in nature. The artist embeds natural materials directly onto her canvases to achieve an archival-like quality—employing a non-dominant perspective that directly confronts the lexicon of historical American landscape artworks. Heymans' paintings explore her childhood memories of playing outdoors with her sister, evoking the meaningful and mystical connections that can be forged with the lands we inhabit and the stories embedded there."),
            Artist(name="Ana Benaroya", medium="painting", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130896786991628401/portrait.jpg", description="Ana Benaroya (b. 1986) is an artist born in New York and raised in New Jersey. She received her MFA in Painting and Printmaking from the Yale School of Art in 2019. From a queer perspective, Benaroya’s work explores notions of power and desire by exaggerating and distorting the human body, playing with its form, and its relationship to other bodies. She draws from the languages of comics, caricature, and pop culture and is influenced by images of bodybuilders, cartoons, gig-posters, and artists such as Tom of Finland, Robert Colescott, the Chicago Imagists as well as children’s artwork. Music and song lyrics often appear in the titles of her works. Benaroya’s work utilizes the subversive power of humor to create an image that at first glance might seem funny and appealing to the eye but upon closer examination, reveals a darker, more serious nature."),
            Artist(name="Laure Mary Couégnias", medium="oil on canvas", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130190532862279862/C9s_nyAWsAY-O42.jpg", description="Laure Mary-Couégnias (b.1989, France) has received her Bachelor and Masters studies from the National School of Fine Arts of Lyon in France. Mary-Couégnias has participated in various solo and group exhibitions. Selected solo exhibitions include ‘Escape Lane’, Richard Heller Gallery, California, USA; ‘Dream Bank’, Domaine de Rouerie, Contemporary Art Center, Sud Hérault, France; ‘Hi, How Are You ?’, Septieme Gallery, Paris, France; ‘Love is a beach’, Contemporary Art Center le Vog, Fontaine, France; ‘J'irai Fleurir sous tes reins’, International Biennale of Contemporary Art, among others. Selected group exhibitions include: ‘Quixotic’, Ramp Gallery, London, United Kingdom; ‘Black & White vs. Color’, Richard Heller Gallery, California, USA; ‘Rendez-vous à la Havane’, Centro de Arte Contemporaneo Wifredo Lam, Havana, Cuba; ‘La Littorale #7’, Chambre(s) d'Amour, curated by Richard Leydier, International Biennale of Contemporary Art of Anglet, Côte Basque, Anglet, France; International Biennale of Contemporary Art of Lyon - Institute of Contemporary Art IAC - Villeurbanne, France; La synchronicité des éléments - CACN, Contemporary Art Center of Nîmes - Nîmes, France. Mary-Couégnias was awarded winner of the visual arts commission at International City of Arts, Paris, France. Her work is featured in numerous public and private collections, such as Association Les Harpailleurs, Switzerland, The Beth Rudin DeWoody Collection, USA, the Château de Courterolles, France, the Domaine de Roueïre, Sud-Hérault, France, The Hall Art Fondation, USA. Mary-Couégnias’s works have been presented by international art publications such as Juxtapoz, Artpress, Elle, Le Monde, among others."),
            Artist(name="Quentin James McCaffrey", medium="oil on canvas, panel", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130189758677651607/img_4150.webp", description="McCaffrey’s worlds are of an arrested time, a stillness emphasizing the activity that is outside its borders. Using single-point perspective, layers of oil paint on panel or canvas, and a focus on light, he renders domestic interior spaces. His motionless interiors seek to call into question the narratives that become ingrained in one’s understanding of the world.McCaffrey’s paintings draw from Quattrocento Italian painting and 17th century Dutch interiors in their use of simple geometry, symbolism, as well as in their stoicism. In western painting, the domestic interior has been a place for investigating the psyche and intimate relationships. Referencing the nostalgia of 19th century academic painting, his paintings allow a space for questioning the forgetful serenity often depicted and acknowledges an undercurrent of a more complex reality. Drawing a parallel between intimate personal experience and imperfect historic narratives, he compares the domestic and psychological interior, and how they are mutually symbolic and influential."),
            Artist(name="Maia Cruz Palileo", medium="oil on panel, canvas", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130911316664660109/MaiaCruzPalileo.jpg", description="Maia Cruz Palileo is a multi-disciplinary, Brooklyn-based artist. Migration and the permeable concept of home are constant themes in their paintings, installations, sculptures, and drawings. Influenced by familial oral histories about migrating to the US from the Philippines alongside the troubling colonial history between the two countries, Maia infuses these narratives using both memory and imagination. When stories and memories are subjected to time and constant retelling, the narratives become questionable, bordering the line between fact and fiction, while remaining cloaked in the convincingly familiar. Maia is a recipient of the Nancy Graves Grant, Art Matters Grant, Joan Mitchell Foundation Painters & Sculptors Grant, Jerome Foundation Travel and Study Program Grant, Rema Hort Mann Foundation Emerging Artist Grant, NYFA Painting Fellowship, Joan Mitchell Foundation MFA Award and the Astraea Visual Arts Fund Award. Maia received an MFA in sculpture from Brooklyn College, City University of New York and BA in Studio Art at Mount Holyoke College, Massachusetts and has participated in residencies at Skowhegan School of Painting and Sculpture, Maine, Lower East Side Print Shop, New York, Millay Colony, New York and the Joan Mitchell Center, New Orleans. They are a recipient of the 2022-23 Sharpe Walentas Studio Program in Brooklyn, NY."),
            Artist(name="Matthew Hansel", medium="painting", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130917586910052369/matthanselartistbiosigning-1643040481437.webp", description="Brooklyn-based artist Matthew Hansel literally and figuratively deconstructs the historical painting, manipulating and folding his canvases to create a surreal and immersive visual experience. Layering imagery from classical painting with warped cartoons and trompe l'oeil figures, Hansel’s work plays with visual absurdity and challenges perspective. Says the artist of his paintings, “These are fake history paintings. More specifically, these are paintings of ceremonies that surround fictitious historic moments. These paintings speak to our need for communal activities and how those activities are being constantly redefined by history."),
            Artist(name="Jennah Meyer", medium="painting", image="https://cdn.discordapp.com/attachments/1113536081091108996/1130937047637573673/IMG_9769.jpg", description="Meyer spent the last 12 years working and living in Paris. She is currently based in New York. The texture and movement of colors and forms in her paintings are inspired by her experiences her in everyday life.")


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
            Artwork(title="You can lay your hands on me", artist_id=3, medium="oil and gloss", style_id=2, image="https://cdn.discordapp.com/attachments/1113536081091108996/1127257306090967100/1650073849-you-can-lay-your-hands-on-me-miranda-forrester.webp"),
            Artwork(title="egocentric with company", artist_id=4, medium="painting", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128462714000380024/IMG_EE27915EE79C-1.jpeg"),
            Artwork(title="The Falling Sky", artist_id=5, medium="colored pencil on wood", style_id=7, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128464073353330829/IMG_4FB6282B24CB-1.jpeg"),
            Artwork(title="To Make Room For The Garden You Must First Burn The House", artist_id=21, medium="oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1130916317369749698/IMG_9328F2C8BD23-1.jpeg"),
            Artwork(title="Get away with it", artist_id=6, medium="oil on canvas", style_id=4, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128465552273317898/IMG_DD18A2944891-1.jpeg"),
            Artwork(title="The secret garden", artist_id=7, medium="oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128467538917982288/IMG_14F16BF868F2-1.jpeg"),
            Artwork(title="detail", artist_id=7, medium="oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128468405373128734/IMG_41CE698A46C5-1.jpeg"),
            Artwork(title="tapas", artist_id=8, medium="acrylic on canvas", style_id=5, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128469403596496966/IMG_6FE0FE3FCD5E-1.jpeg"),
            Artwork(title="my face for the world to see", artist_id=9, medium="painting", style_id=7, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128471497963475074/IMG_54ACA6E2DC69-1.jpeg"),
            Artwork(title="Chorus", artist_id=10, medium="painting", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128472079801532516/IMG_704D411FB1B3-1.jpeg"),
            Artwork(title="Morning Glory", artist_id=11, medium="painting", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128473376839708702/IMG_52F56975D1A0-1.jpeg"),
            Artwork(title="Tell me more", artist_id=11, medium="painting", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1130914307648004188/VO1022_FOB_McKinney_03.webp"),
            Artwork(title="untitled", artist_id=12, medium="print", style_id=4, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128473889475924070/IMG_07E4D9373890-1.jpeg"),
            Artwork(title="Circa", artist_id=13, medium="painting", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128476093939195984/IMG_BD46ABE633B0-1.jpeg"),
            Artwork(title="Downward Dog", artist_id=14, medium="acrylic on wood", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128477120650301520/IMG_5A69CE0B82F5-1.jpeg"),
            Artwork(title="Paper Angel", artist_id=14, medium="acrylic on wood panel", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128477791868948571/IMG_CF6B99484656-1.jpeg"),
            Artwork(title="Courts (meditation in black)", artist_id=15, medium="oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128485218047754240/IMG_C59F46881C3F-1.jpeg"),
            Artwork(title="Reverie in Blue (Kayla)", artist_id=15, medium="oil on linen", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1130913557949730866/Screenshot_2023-07-18_at_1.26.06_PM.png"),
            Artwork(title="Fallen Daughters", artist_id=16, medium="papier mache, molding paste, multimedia, oil on canvas", style_id=2, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128484369405837453/IMG_CF8BDFADF28E-1.jpeg"),
            Artwork(title="A Full Moon", artist_id=17, medium="painting", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128697183076614246/AnaBenaroya_AFullMoon.jpg"),
            Artwork(title="By The Ocean's Roar", artist_id=17, medium="painting", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1128698800219881552/ABENA015_001.jpg"),
            Artwork(title="Everything but...", artist_id=18, medium="painting, oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1129854458461958235/image.png"),
            Artwork(title="The Time of the Beginning", artist_id=18, medium="painting, oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1129855275822756000/image.png"),
            Artwork(title="Hour of light", artist_id=19, medium="oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1129876930401947810/image.png"),
            Artwork(title="Magic Fire", artist_id=20, medium="oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1130912898626109480/1599090_MagicFire.jpg"),
            Artwork(title="As Above, So Below - As For Love? No One Knows", artist_id=21, medium="oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1130915708390359040/IMG_F2BEC11B030E-1.jpeg"),
            Artwork(title="Jazz Players", artist_id=22, medium="oil on canvas", style_id=1, image="https://cdn.discordapp.com/attachments/1113536081091108996/1130936590848491530/IMG_9768.jpg")
           
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
