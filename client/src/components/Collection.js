import React from "react";

function Collection() {
  // Fetch or get the collection of artworks from your data source or state

  // Example collection of artworks
  const collection = [
    { id: 1, title: "Artwork 1" },
    { id: 2, title: "Artwork 2"},
    { id: 3, title: "Artwork 3" },
    // Add more artworks to the collection
  ];
//   const collection = [
//     { id: 1, title: "Artwork 1", image: "artwork1.jpg" },
//     { id: 2, title: "Artwork 2", image: "artwork2.jpg" },
//     { id: 3, title: "Artwork 3", image: "artwork3.jpg" },
//     // Add more artworks to the collection
//   ];

  return (
    <div>
      <h1>My Art Collection</h1>
      {collection.map((artwork) => (
        <div key={artwork.id}>
          <h2>{artwork.title}</h2>
          <img src={artwork.image} alt={artwork.title} style={{ maxWidth: "400px", maxHeight: "400px" }} />
        </div>
      ))}
    </div>
  );
}

export default Collection;