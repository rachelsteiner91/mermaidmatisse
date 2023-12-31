import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import Modal from "react-modal";
import { Link } from "react-router-dom";

function ArtDetail() {
  const [artwork, setArtwork] = useState({
    roles: [],
    artists: {},
    style: {}
  });
  const [error, setError] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false); 
  const [zoomLevel, setZoomLevel] = useState(1); 

  const params = useParams();

  useEffect(() => {
    fetch(`/artworks/${params.id}`)
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

  const { id, title, image, artists, artist_id, medium, style } = artwork;
  console.log(artwork)

  if (error) return <h2>{error}</h2>;

  const handleImageClick = () => {
    setIsModalOpen(true); 
  };

  const closeModal = () => {
    setIsModalOpen(false); 
    setZoomLevel(1); 
  };

  const handleZoomIn = () => {
    setZoomLevel(prevZoomLevel => prevZoomLevel + 0.1); 
  };

  const handleZoomOut = () => {
    setZoomLevel(prevZoomLevel => Math.max(prevZoomLevel - 0.1, 1));
  };

  return (
    <div className="art-detail" id={id}>
      <Link to="/artworks">
        <h3>Back to Art</h3>
        </Link>
      <h2>{title}</h2>
      <Link to={`/artists/${artist_id}`}>
      <p>{artists.name}</p>
      </Link>
     
      
      <p style={{fontSize: '12px', fontStyle: 'italic'}}>*click on artwork image to zoom in* </p>

      <div className="project-card">
        <figure className="image">
          <img
            src={image}
            alt={title}
            style={{ maxWidth: "600px", maxHeight: "600px", cursor: "zoom-in" }}
            onClick={handleImageClick} 
          />
          <section>
            <p> {artists.name}</p>
            <p> {medium}</p>
            <p> {style.style_type}</p>
          </section>
        </figure>
        <section className="details"></section>
      </div>

  
      <Modal isOpen={isModalOpen} onRequestClose={closeModal} ariaHideApp={false}>
        <button onClick={closeModal} className="close-button">Close</button>
        <div className="modal-image-container">
          <img
            src={image}
            alt={title}
            style={{ transform: `scale(${zoomLevel})` }} 
          />
          <div className="zoom-controls">
            <button onClick={handleZoomIn} className="zoom-button">+</button>
            <button onClick={handleZoomOut} className="zoom-button">-</button>
          </div>
        </div>
      </Modal>
    </div>
  );
}

export default ArtDetail;





