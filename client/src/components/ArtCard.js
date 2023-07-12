import React, { useState } from "react";
import { Link } from "react-router-dom";

// NOTE - THE BUTTON TO ADD TO COLLECTION NEEDS TO BE ROUTED TO COLLECTIONS/:ID INSTREAD
function ArtCard({ artwork, addToCollection }) {
  const { id, title, image, artists, medium, style } = artwork;
  const [isAdded, setIsAdded] = useState(false);

  const handleAddToCollection = () => {
    setIsAdded(true);
    addToCollection(artwork);
 
  };
  // if (isAdded) {
  //   return <Link to="/collections/:id">Go to Collections</Link>;
  // }

  return (
   
    <div className="card" id={id}  >
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
          <p>Collected Artwork!
            <Link to="/collections">Go to Collections</Link>
          </p>
          
        )}
      </section>
    </div>
    
  );
}

export default ArtCard;