import React from "react";
import {  Link, NavLink } from "react-router-dom";
import Search from './Search'
// import NavBar from './NavBar';

// TO DO TODAY WEDNESDAY 
//auth login
// collection part
//favorites button maybe? add to collection



function Nav() {
  // maybe the search should actually be in App? ask Greem
  // const [search, setSearch] = useState('')

//   const handleSearch = (newStr) => {
//     setSearch(newStr)
//   }

//  const filteredArts = [...artworks].filter(artwork =>
//     artwork.name.toLowerCase().includes(search.toLowerCase()))
// search={search} handleSearch={handleSearch}
  return (
    
      <header>
        <h1 className="extra-bold">
          Mermaid Matisse
          <span className="logo" role="img"></span>
        </h1>
        <h1>
          <Link to={"/"}></Link>
        </h1>
        <Search />
        <div className="menu" >
          <NavLink className="button" to="/">
            Home
          </NavLink>
          <NavLink className="button" to="/artworks">
            View All
          </NavLink>
          <NavLink className="button" to="/artists">
            Artists
          </NavLink>
          <NavLink className="button" to="/styles">
            By Style
          </NavLink>
          <NavLink className="button" to="/collections">
            Collection
          </NavLink>
          <NavLink className="button" to="/signup">
            Artwork Discovery
          </NavLink>
          <NavLink className="button" to="/staffpicks">
            Staff Picks
          </NavLink>
          <NavLink className="button" to="/about">
            About Us
          </NavLink>
        </div>
      </header>
    
  );
}

export default Nav;
