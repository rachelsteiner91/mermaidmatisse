import ArtistCard from './ArtistCard'
// import {useNavigate} from "react-router-dom"

function Artist({ artists}) {
    return (
        <section>
            <ul className='artistcards' style={{ marginTop: '50px', display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '10px' }}>
                {artists.map(artist => <ArtistCard key={artist.id} artist={artist} />)}
            </ul>
        </section>
    )
}

export default Artist