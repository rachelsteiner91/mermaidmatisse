import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function ArtistDetail() {
  const [artist, setArtist] = useState({});
  const [error, setError] = useState(null);

  const params = useParams();

  useEffect(() => {
    fetch(`/artists/${params.id}`)
      .then((res) => {
        if (res.ok) {
          return res.json();
        } else {
          throw new Error("Failed to fetch artist");
        }
      })
      .then((data) => setArtist(data))
      .catch((error) => setError(error.message));
  }, [params.id]);

  const { id, name, medium, image, description } = artist;

  if (error) return <h2>{error}</h2>;

  return (
    <div className="style-detail" id={id}>
      <Link to="/artists">
        <h3>Back to Artists</h3>
        </Link>
        <Link to="/artworks">
        <h3>Back to Artworks</h3>
        </Link>
      <h1>{name}</h1>
      <div className="centered-container">
      <div className="style-card">
        <figure className="image" >
          <img src={image} alt={description}  style={{ maxWidth: "600px", maxHeight: "600px" }}/>
          <section style={{ maxWidth: "600px", maxHeight: "600px",textAlign: "justify"  }}>
            <p> {description}</p>
            <p>  {medium}</p>
          

          </section>
        </figure>
        <section className="details">{/* Additional details here */}</section>
      </div>
    </div>
    </div>
  );
}

export default ArtistDetail;