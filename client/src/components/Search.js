import React from 'react';


function Search(){

    return(
        <div className="search-container">
        <input type="text" placeholder="Search by style" />
        <button type="button">Search</button>
      </div>
    );
  }

export default Search

// function Search({setSearch, search}) {
//     function handleChange(e) {
//         setSearch(e.target.value)
//     }
//   return (
//     <div className="ui search"> 
//         <div className="ui icon input">
//         <label htmlFor="Search"> Search by color, style, artist, mood...:</label>
//         <input
//             value={search}
//             type="text"
//             id="search"
//             placeholder="Search by city, or by park..."
//             onChange={(e) => handleChange(e)}
//         />
//         <button type="button">Search</button>
// </div>
//     </div>
//   )
// }

// export default Search