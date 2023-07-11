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

