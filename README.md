## MERMAID MATISSE
The Tinder for emerging art discovery. Tap into the art world with a simple, and powerful web and mobile-centric tool that helps you easily swipe to discover and virtually 'collect' art. This platform is for people who are open to learning about lesser known artists and want to trust their own decisions based off of what they like, and their tastes. 
Users will be shown an assortment of images, mainly paintings, prints and other mediums of art -- based on their selections, this will bring them to the next phase in the funnel which will resemble that of a feed displaying various works by emerging artists.
The user, which we call “curator” has the ability to create their own tailored art collection and feed of favorites, through the familiar action of a ‘like’ or 'collect art'. 
The goal is to guide you (the curator) to discover art in a fun, engaging and accessible way.

![Screenshot 2023-07-20 at 1 38 27 PM](https://github.com/rachelsteiner91/mermaidmatisse/assets/127536637/252dfd82-c2a1-4a9b-a51a-901bac576fe0)

<img width="1356" alt="Screenshot 2023-07-18 at 7 16 21 PM" src="https://github.com/rachelsteiner91/mermaidmatisse/assets/127536637/6f203ca3-f509-4db7-ab13-fbd10afc283f">

## User Stories 
- Users can view all artworks
- Users can search and view by color, medium, subject matter(minimalist, abstract, contemporary, human, landscape), staff picks
- Users can add artworks to their art collection 
- Users can delete or thumbs down an artwork they don't like

## Models
https://dbdiagram.io/d/64a3166702bd1c4a5e6e71dc
![Screenshot 2023-07-05 at 3 15 42 PM](https://github.com/rachelsteiner91/mermaidmatisse/assets/127536637/a144b654-a0d7-40e5-ad4a-67ac2e2d55ff)


##User
- belongs to a Collection
- has many Artworks through ArtCollections
- has a Collection through ArtCollections
- has many Artworks
  
##Artwork
- belongs to an Artist
- has many Collections

##Artist
- has many Artworks

##Collection
- belongs to a User
- has many Artworks 


## API Routes
| API Route           | Method | Body                         | Response |
|---------------------|--------|------------------------------|----------|
| /users              | GET    |                              |          |
| /users              | POST   | create a new user login      |          |
| /users/int:id       | GET    | specific user                |          |
| /artists            | GET    | view all artists in database |          |
| /artists/int:id     | GET    | view specific artist         |          |
| /artworks           | GET    | view all artworks            |          |
| /artworks/int:id    | GET    | view one artwork             |          |
| /artworks/int:id    | DELETE | remove artwork from view     |          |
| /collections        | POST   | create a new collection      |          |
| /collections/int:id | PATCH  | add or update collection     |          |
| /collection/int:id  | GET    | view user collection         |          |
| /styles/int:id      | GET    | view one style               |          |
| /styles             | GET    | view all styles              |          |

## Wireframe
https://www.figma.com/file/oI7mVHO4AIwjU5yEBXPglR/Mermaid-Matisse---Capstone?type=design&node-id=0%3A1&mode=design&t=q7z1q2s3K8roI7l0-1
![Screenshot 2023-07-05 at 11 40 19 AM](https://github.com/rachelsteiner91/mermaidmatisse/assets/127536637/d14c2231-fd8a-4947-8d6e-43cdd50caf62)

## Trello
https://trello.com/b/RkIgk0YV/kanban-template



## Resources

- [Setting up a respository - Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
- [Create a repo- GitHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
- [Python Circular Imports - StackAbuse](https://stackabuse.com/python-circular-imports/)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)
