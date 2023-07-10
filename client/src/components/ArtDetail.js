import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";

function ArtDetail() {
  const [artwork, setArtwork] = useState({
    roles: [],
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

  

  const { id, title, image, artist_id, medium, style_id } = artwork;

  if (error) return <h2>{error}</h2>;

  return (
    <div className="art-detail" id={id}>
      <h1>{title}</h1>
      <p>{artist_id}</p>

      <div className="project-card">
        <figure className="image">
          <img src={image} alt={title} />
          <section>
            <p>Style: {style_id}</p>
            <p>Artist: {artist_id}</p>
            <p>Medium: {medium}</p>
          </section>
        </figure>
        <section className="details">
          {/* <h3 style={{ margin: "16px auto" }}>Cast: </h3>
          <ul className="crew">
            {artwork.roles.map((crew) => (
              <li key={crew.actor.id}>
                <img
                  width={"100px"}
                  src={crew.actor.image}
                  alt={crew.actor.name}
                />
                <div className="artist">
                  <Link to={`/artists/${crew.actor.id}`}>
                    <p style={{ fontStyle: "italic" }}>{crew.actor.name}</p>
                  </Link>
                </div>
              </li>
            ))}
          </ul> */}
        </section>
      </div>
    </div>
  );
}

export default ArtDetail;