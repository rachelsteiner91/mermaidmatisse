import { Link } from "react-router-dom";

function StyleCard({ style }) {
    const { style_type, id } = style;

  return (
    <li className="card" id={id}>
    <figure className="style">
       
    </figure>
    <section className="details">
        <Link to={`/styles/${id}`}>
            <h2>{style_type}</h2>
        </Link>
        <p>Styles</p>
    </section>
</li>
  )
}


export default StyleCard