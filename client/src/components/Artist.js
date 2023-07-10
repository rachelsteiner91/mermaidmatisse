import ArtistCard from './ArtistCard'
// import {useNavigate} from "react-router-dom"

function Artist({ artists}) {
    return (
        <section>
            <ul className='artistcards'>
                {artists.map(artist => <ArtistCard key={artist.id} artist={artist} />)}
            </ul>
        </section>
    )
}

export default Artist