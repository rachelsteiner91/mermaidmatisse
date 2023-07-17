import { Link } from "react-router-dom";
import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css";

function HomePage({artworks}){
   
    return(
        <div>
          <Link to="/artworks">
            <h3>Discover Art</h3>
            </Link> 
            <h3>New Arrivals</h3>
            

      
      <div id="carouselExampleControls" className="carousel slide" data-bs-ride="carousel">
        <div className="carousel-inner">
          <Carousel autoPlay={true} infiniteLoop={true} interval={5000}>
          {artworks.map((artwork, index) => (
             <div className={`carousel-item ${index === 0 ? 'active' : ''}`} key={index}>
             <img src={artwork.image} className="carousel-image" alt={`Artwork ${index + 1}`} style={{ maxWidth: '500px', maxHeight: '500px' }} />
             <section>
             <div className="carousel-text">
            <p style={{  fontSize: '12px' }}>{artwork.artists.name}, {artwork.title}</p> 
            <p style={{ marginTop: '30px' }}></p>
          </div>
             </section> 
           </div>
         ))}
         
          </Carousel>
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
     
<div className="image-grid" style={{ marginTop: '30px', display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '10px' }}>
        {artworks.map((artwork, index) => (
          <img key={index} src={artwork.image} alt={`Artwork ${index + 1}`} className="grid-image" style={{ width: '100%', height: 'auto' }} />
        ))}
      </div>
    </div>
  );
}



export default HomePage




// <Carousel
//         renderArrowPrev={(onClickHandler, hasPrev, label) =>
//           hasPrev && (
//             <button type="button" onClick={onClickHandler} title={label}>
//               Previous
//             </button>
//           )
//         }
//         renderArrowNext={(onClickHandler, hasNext, label) =>
//           hasNext && (
//             <button type="button" onClick={onClickHandler} title={label}>
//               Next
//             </button>
//           )
//         }
//       ></Carousel>