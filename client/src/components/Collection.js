import React from "react";

function Collection({ collection }) {
    //   const collection = [
//     { id: 1, title: "Artwork 1" },
//     { id: 2, title: "Artwork 2"},
//     { id: 3, title: "Artwork 3" },
   
//   ];
  return (
    <div>
      <h1>My Art Collection</h1>
      {collection.map((artwork) => (
        <div key={artwork.id}>
          <h2>{artwork.title}</h2>
          <img
            src={artwork.image}
            alt={artwork.artists.name}
            style={{ maxWidth: "400px", maxHeight: "400px" }}
          />
        </div>
      ))}
    </div>
  );
}

export default Collection;

// function Collection() {
  
//   const collection = [
//     { id: 1, title: "Artwork 1" },
//     { id: 2, title: "Artwork 2"},
//     { id: 3, title: "Artwork 3" },
   
//   ];


//   return (
//     <div>
//       <h1>My Art Collection</h1>
//       {collection.map((artwork) => (
//         <div key={artwork.id}>
//           <h2>{artwork.title}</h2>
//           <img src={artwork.image} alt={artwork.title} style={{ maxWidth: "400px", maxHeight: "400px" }} />
//         </div>
//       ))}
//     </div>
//   );
// }

// export default Collection;