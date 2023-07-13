import { Link } from "react-router-dom";

function StyleCard({ style }) {
    const { style_type, id } = style;

  return (
    <div className="card" id={id}>
    <figure className="style">
       
    </figure>
    <section className="details">
        <Link to={`/styles/${id}`}>
            <h2>{style_type}</h2>
        </Link>
        <p>Insert Images here</p>
    </section>
</div>
  )
}


export default StyleCard