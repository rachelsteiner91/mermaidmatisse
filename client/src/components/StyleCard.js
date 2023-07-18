import { Link } from "react-router-dom";

function StyleCard({ style }) {
    const { style_type, id } = style;

  return (
    
    <div className="card" id={id}>
      <h2>Coming Soon...</h2>
    <figure className="style">
       
    </figure>
    <section className="details">
        <Link to={`/styles/${id}`}>
            <h3>{style_type}</h3>
        </Link>
        <p>Insert Images here</p>
    </section>
</div>
  )
}


export default StyleCard