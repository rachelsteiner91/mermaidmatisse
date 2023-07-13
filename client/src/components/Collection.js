import { Link } from "react-router-dom";

function Collection({ collection }) {
    //   const collection = [
//     { id: 1, title: "Artwork 1" },
//     { id: 2, title: "Artwork 2"},
//     { id: 3, title: "Artwork 3" },
   
//   ];
  return (
    <div>
        <Link to="/artworks">
        <h3>Back to Art</h3>
        </Link>
        <Link to="/collections:id">
      <h1>My Art Collection</h1>
      </Link>
      {collection.map((artwork, index) => (
        <div key={index}>
          <h2>{artwork.title}</h2>
          <img
            src={artwork.image}
            alt={artwork.title}
            style={{ maxWidth: "400px", maxHeight: "400px" }}
          />
        </div>
      ))}
    </div>
  );
}

export default Collection;

// {
//     "artwork_id": 1,
//     "id": 1,
//     "user_id": 1
// }

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