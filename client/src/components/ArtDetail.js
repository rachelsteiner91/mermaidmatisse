import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";

function ArtDetail() {
  const [artwork, setArtwork] = useState({
    roles: [],
    artists: {},
    style: {}
  });
  const [error, setError] = useState(null);

  const params = useParams();

  useEffect(() => {
    fetch(`http://localhost:5555/artworks/${params.id}`)
      .then((res) => {
        if (res.ok) {
          return res.json();
        } else {
          throw new Error("Failed to fetch artwork");
        }
      })
      .then((data) => setArtwork(data))
      .catch((error) => setError(error.message));
  }, [params.id]);

  

  const { id, title, image, artists, medium, style } = artwork;

  if (error) return <h2>{error}</h2>;

  return (
    <div className="art-detail" id={id}>
      <h1>{title}</h1>
      <p>{artists.name}</p>

      <div className="project-card">
        <figure className="image">
        <img src={image} alt={title} style={{ maxWidth: "400px", maxHeight: "400px" }} />
          <section>
            <p>Style: {style.style_type}</p>
            <p>Artist: {artists.name}</p>
            <p>Medium: {medium}</p>
          </section>
        </figure>
        <section className="details">
          
        </section>
      </div>
    </div>
  );
}

export default ArtDetail;

