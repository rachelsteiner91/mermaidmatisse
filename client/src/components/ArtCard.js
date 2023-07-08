import { Link } from "react-router-dom";

function ArtCard({ artwork }) {
    const { title, image, medium, style_id, artist_id, id } = artwork;

  return (
    <li className="card" id={id}>
    <figure className="image">
        <img src={image} alt={artist_id} />
    </figure>
    <section className="details">
        <Link to={`/artworks/${id}`}>
            <h2>{title}</h2>
        </Link>
        <p>{medium}, {style_id}</p>
    </section>
</li>
  )
}


export default ArtCard

// function ArtCard({artwork}) {
    

//     return(
//         <div>
//         <ul className= "artcard" id={artwork.id}>
//             <li>
//             <img src={artwork.image} alt={artwork.title} />
//             </li>
//         </ul>
//         </div>
//     )
// }