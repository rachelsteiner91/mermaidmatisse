
import ArtCard from './ArtCard'

// import {useNavigate} from "react-router-dom"

function ArtContainer({ artworks, addToCollection}) {
   
    return (
        <section>
            <ul className='cards'>
                {artworks.map(artwork => <ArtCard key={artwork.id} artwork={artwork} addToCollection={addToCollection} />)}
                
            </ul>
        </section>
    )
}

export default ArtContainer

