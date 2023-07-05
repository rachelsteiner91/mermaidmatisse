## MERMAID MATISSE

## About Mermaid Matisse
The Tinder for art world discovery

## User Stories 
- Users can view all artworks
- Users can add artworks to their art collection
- Users can delete or thumbs down an artwork they don't like

## Models
https://dbdiagram.io/d/64a3166702bd1c4a5e6e71dc
![Screenshot 2023-07-05 at 1 26 27 PM](https://github.com/rachelsteiner91/mermaidmatisse/assets/127536637/3d30f981-fe6d-4418-88e5-7bcb146bfe0c)

# a User
- belongs to a Collection
- has many Artworks through ArtCollections
- has a Collection through ArtCollections
- has many Artworks
- 
# an Artwork
- belongs to an Artist
- has many Collections

# an Artist
- has many Artworks

# a Collection
- belongs to a User
- has many Artworks through an ArtCollection


## API Routes

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
