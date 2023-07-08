import ArtCard from './ArtCard'
// import {useNavigate} from "react-router-dom"

function ArtContainer({ artworks}) {
    return (
        <section>
            <ul className='cards'>
                {artworks.map(artwork => <ArtCard key={artwork.id} artwork={artwork} />)}
            </ul>
        </section>
    )
}

export default ArtContainer


// function ArtContainer({artworks}) {
//     const validArt = artworks.filter(artwork => artwork.id != null)
//     const artCards = validArt.map(artwork => (
//     <ArtCard
//     key={artwork.id}
//     artwork={artwork}
// />
// ));
//   return (
//     <div className="ArtworksList"> View Artworks {artCards}
     
//     </div>
// )
// }
//  {/*adventurer card*/}
//  {
//     [...artworks].map((el) => {
//       return <ArtCard key = {el.id} artwork={el} />
//     })
//   }