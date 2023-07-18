import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";

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

  const { id, name, medium } = artist;

  if (error) return <h2>{error}</h2>;

  return (
    <div className="style-detail" id={id}>
      <h1>{name}</h1>

      <div className="style-card">
        <figure className="image">
          {/* <img src={image} alt={title} /> */}
          <section>
            <p>Artist: {name}</p>
            <p> Medium: {medium}</p>
          </section>
        </figure>
        <section className="details">{/* Additional details here */}</section>
      </div>
    </div>
  );
}

export default ArtistDetail;