import React, { useState, useContext } from "react";
import UserContext from "../UserContext";
import { Link } from "react-router-dom";

// NOTE - THE BUTTON TO ADD TO COLLECTION NEEDS TO BE ROUTED TO COLLECTIONS/:ID INSTREAD
function ArtCard({ artwork, addToCollection }) {
  const { id, title, image, artists, medium, style } = artwork;
  const [isAdded, setIsAdded] = useState(false);
  const {user} = useContext(UserContext)
  console.log(user)

  const handleAddToCollection = () => {
    fetch("/collections", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        "artwork_id": artwork.id
      }),
    })
    setIsAdded(true);
    addToCollection(artwork);
 
  };
  // if (isAdded) {
  //   return <Link to="/collections/:id">Go to Collections</Link>;
  // }

//  style= {{ maxWidth: "400px", maxHeight: "400px" }}

  return (
   
    <div className="card" id={id} >
      <figure className="image" >
      <Link to={`/artworks/${id}`}>
        <img
          src={image}
          alt={artists.name}
          style={{ width: '100%', height: 'auto' }}
        />
        </Link>
      </figure>
      <section className="details" style={{ width: '100%', height: 'auto' }}>
        <h2 style={{fontSize: '14px', fontWeight: 'bold'}}>{artists.name}</h2> 
        <p style={{fontSize: '14px'}}> {title}</p> 
        <p  style={{fontSize: '12px', fontStyle: 'italic'}}> {medium}, {style.style_type} </p>
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

