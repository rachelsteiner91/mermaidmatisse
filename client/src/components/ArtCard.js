// import { Link } from "react-router-dom";

// function ArtCard({ artwork }) {
//     const { title, image, medium, style_id, artist_id, id } = artwork;

//   return (
//     <li className="card" id={id}>
//     <figure className="image">
//         <img src={image} alt={artist_id} style={{ maxWidth: "400px", maxHeight: "400px" }}/>
//     </figure>
//     <section className="details">
//         <Link to={`/artworks/${id}`}>
//             <h2>{title}</h2>
//         </Link>
//         <p>{medium}, {style_id}</p>
//     </section>
// </li>
//   )
// }

// export default ArtCard
import { useState } from "react";
import { Link } from "react-router-dom";

function ArtCard({ artwork }) {
  const {id, title, image, artists, medium, style } = artwork;
  const [isAdded, setIsAdded] = useState(false);
  

  const handleAddToCollection = () => {
    

    setIsAdded(true);

    
  
  };

  return (
    <li className="card" id={id}>
      <figure className="image">
        <img
          src={image}
          alt={artists.name}
          style={{ maxWidth: "400px", maxHeight: "400px" }}
        />
      </figure>
      <section className="details">
        <Link to={`/artworks/${id}`}>
          <h2>{title}</h2>
        </Link>
        <p>
        {artists.name}, {medium}, {style.style_type}
        </p>
        {!isAdded ? (
          <button onClick={handleAddToCollection}>Add to Art Collection</button>
        ) : (
          <p>Added to Art Collection!</p>
        )}
      </section>
    </li>
  );
}

export default ArtCard;
