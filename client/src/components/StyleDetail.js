import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";

function StyleDetail() {
  const [style, setStyle] = useState({});
  const [error, setError] = useState(null);

  const params = useParams();

  useEffect(() => {
    fetch(`/styles/${params.id}`)
      .then((res) => {
        if (res.ok) {
          return res.json();
        } else {
          throw new Error("Failed to fetch style");
        }
      })
      .then((data) => setStyle(data))
      .catch((error) => setError(error.message));
  }, [params.id]);

  const { id, style_type } = style;

  if (error) return <h2>{error}</h2>;

  return (
    <div className="style-detail" id={id}>
      <h1>{style_type}</h1>

      <div className="style-card">
        <figure className="image">
          {/* <img src={image} alt={title} /> */}
          <section>
            <p>Style: {style_type}</p>
          </section>
        </figure>
        <section className="details">{/* Additional details here */}</section>
      </div>
    </div>
  );
}

export default StyleDetail;


// import { useParams } from "react-router-dom";
// import { useEffect, useState } from "react";

// function StyleDetail() {
//   const [style, setStyle] = useState({
//     roles: [],
//   });
//   const [error, setError] = useState(null);

//   const params = useParams();

//   useEffect(() => {
//     fetch(`/styles/${params.id}`)
//       .then((res) => {
//         if (res.ok) {
//           return res.json();
//         } else {
//           throw new Error("Failed to fetch style");
//         }
//       })
//       .then((data) => setStyle(data))
//       .catch((error) => setError(error.message));
//   }, [params.id]);

  

//   const { id, style_type } = style;

//   if (error) return <h2>{error}</h2>;

//   return (
//     <div className="style-detail" id={id}>
//       <h1>{style_type}</h1>
     

//       <div className="style-card">
//         <figure className="image">
//           {/* <img src={image} alt={title} /> */}
//           <section>
//             <p>Style: {style_type}</p>
           
//           </section>
//         </figure>
//         <section className="details">
       
//         </section>
//       </div>
//     </div>
//   );
// }

// export default StyleDetail;