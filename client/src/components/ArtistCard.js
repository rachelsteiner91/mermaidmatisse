import { Link } from "react-router-dom";
import {useState} from "react";

function ArtistCard({ artist }) {
    const { name, medium, id, image, description } = artist;
    const [showDescription, setShowDescription] = useState(false);

    const toggleDescription = () => {
      setShowDescription((prevState) => !prevState);
    }

  return (
    <div className="card" id={id} >
    {/* <li className="card" id={id}> */}
    <figure className="artist">
       
    </figure>
    <section className="details" >
        <img
            src={image}
            alt={description}
            style={{ maxWidth: "400px", maxHeight: "400px", cursor: "pointer" }}
            onClick={toggleDescription}
          />
          <Link to={`/artists/${id}`}>
            <h2>{name}</h2>
            </Link>
        
        <p>{medium}</p>
        {showDescription && <p style={{textAlign: 'justify'}}>{description}</p>}
        {/* <p>{description}</p> */}
    </section>
</div>
  )
}


export default ArtistCard