import React from 'react';
// import { Link } from "react-router-dom"

function ArtCard({artwork}) {
    

    return(
        <div>
        <ul className= "artcard" id={artwork.id}>
            <li>
            <img src={artwork.image} alt={artwork.title} />
            </li>
        </ul>
        </div>
    )
}


export default ArtCard