import React from 'react'


function HomePage({artworks}){
   
    return(
        <div>
            <h1>home</h1>
            <h3>Staff Picks</h3>

      {/* Carousel */}
      <div id="carouselExampleControls" className="carousel slide" data-bs-ride="carousel">
        <div className="carousel-inner">
          {artworks.map((artwork, index) => (
            <div className={`carousel-item ${index === 0 ? 'active' : ''}`} key={index}>
              <img src={artwork.image} className="carousel-image" alt={`Artwork ${index + 1}`} style={{ maxWidth: '500px', maxHeight: '400px' }} />
            </div>
          ))}
        </div>
        <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
          <span className="carousel-control-prev-icon" aria-hidden="true"></span>
          <span className="visually-hidden">Previous</span>
        </button>
        <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
          <span className="carousel-control-next-icon" aria-hidden="true"></span>
          <span className="visually-hidden">Next</span>
        </button>
      </div>
      {/* <div id="carouselExampleControls" className="carousel slide" data-bs-ride="carousel">
        <div className="carousel-inner">
          {artworks.map((artwork, index) => (
            <div className={`carousel-item ${index === 0 ? 'active' : ''}`} key={index}>
              <img src={artwork.image} className="d-block w-100" alt={`Artwork ${index + 1}`} />
            </div>
          ))}
        </div>
        <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
          <span className="carousel-control-prev-icon" aria-hidden="true"></span>
          <span className="visually-hidden">Previous</span>
        </button>
        <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
          <span className="carousel-control-next-icon" aria-hidden="true"></span>
          <span className="visually-hidden">Next</span>
        </button>
      </div> */}

      {/* Image Grid */}
      {/* <div className="image-grid">
        {artworks.map((artwork, index) => (
          <img key={index} src={artwork.image} alt={`Artwork ${index + 1}`} />
        ))}
      </div>
    </div>
  );
} */}
<div className="image-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '10px' }}>
        {artworks.map((artwork, index) => (
          <img key={index} src={artwork.image} alt={`Artwork ${index + 1}`} className="grid-image" style={{ width: '100%', height: 'auto' }} />
        ))}
      </div>
    </div>
  );
}



export default HomePage