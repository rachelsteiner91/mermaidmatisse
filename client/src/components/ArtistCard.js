import { Link } from "react-router-dom";

function ArtistCard({ artist }) {
    const { name, medium, id } = artist;

  return (
    <div className="card" id={id}>
    {/* <li className="card" id={id}> */}
    <figure className="artist">
       
    </figure>
    <section className="details">
        <Link to={`/artists/${id}`}>
            <h2>{name}</h2>
        </Link>
        <p>{medium}</p>
    </section>
</div>
  )
}


export default ArtistCard