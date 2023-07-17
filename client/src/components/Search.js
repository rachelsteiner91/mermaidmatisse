import React from "react";

function Search({search, onSearchChange}) {

  return (
    <div className="searchbar" style={{ display: 'flex', alignItems: 'center' }}>
      <label htmlFor="search"></label>
      <input
        value={search}
        type="text"
        id="search"
        placeholder="Search..."
        onChange={(e) => onSearchChange(e.target.value)} 
        style={{ background: '#EEE9E9' }}
      />
    </div>
  );
}

export default Search;

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
//             placeholder="Search by style..."
//             onChange={(e) => handleChange(e)}
//         />
//         <button type="button">Search</button>
// </div>
//     </div>
//   )
// }

// export default Search