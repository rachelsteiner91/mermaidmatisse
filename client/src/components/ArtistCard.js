import { Link } from "react-router-dom";

function ArtistCard({ artist }) {
    const { name, medium, id, image, description } = artist;

  return (
    <div className="card" id={id}>
    {/* <li className="card" id={id}> */}
    <figure className="artist">
       
    </figure>
    <section className="details">
        <Link to={`/artists/${id}`}>
        <img
            src={image}
            alt={description}
            style={{ maxWidth: "400px", maxHeight: "400px" }}
          />
          </Link>
            <h2>{name}</h2>
        
        <p>{medium}</p>
        <p>{description}</p>
    </section>
</div>
  )
}


export default ArtistCard