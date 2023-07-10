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
  const { title, image, medium, style_id, artist_id, id } = artwork;
  const [isAdded, setIsAdded] = useState(false);
  // const history = useHistory();

  const handleAddToCollection = () => {
    // Add your logic here to handle adding the artwork to the collection

    setIsAdded(true);

    // Navigate to "/collections" route
    // history.push("/collections");
  };

  return (
    <li className="card" id={id}>
      <figure className="image">
        <img
          src={image}
          alt={artist_id}
          style={{ maxWidth: "400px", maxHeight: "400px" }}
        />
      </figure>
      <section className="details">
        <Link to={`/artworks/${id}`}>
          <h2>{title}</h2>
        </Link>
        <p>
          {medium}, {style_id}
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
