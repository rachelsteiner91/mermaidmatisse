import StyleCard from './StyleCard';

function ByStyle({styles}) {
    
   

return (
    <section>
    <ul className='style'>
        {styles.map(style => <StyleCard key={style.id} style={style} />)}
    </ul>
    </section>

    // <li className="style" >
  
    // <Link to={`/styles`}>
    // <h2>{style_type}</h2>
    // </Link>
    // </li>
    // </section>
)}


export default ByStyle;

// return (
//     <li className="style" >
  
//     <Link to={`/styles/${id}`}>
//     <h2>{style_type}</h2>
//     </Link>
//     </li>
// )}

// export default ByStyle;

