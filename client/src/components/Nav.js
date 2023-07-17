import React from "react";
import {  Link, NavLink } from "react-router-dom";

// import NavBar from './NavBar';

// TO DO TODAY WEDNESDAY 
//auth login
// collection part
//favorites button maybe? add to collection



function Nav() {
  // maybe the search should actually be in App? ask Greem
  // const [search, setSearch] = useState('')


  return (
    
      <header>
        {/* <h1 className="extra-bold">
          Mermaid Matisse
          <span className="logo" role="img"></span>
        </h1> */}
        <h1>
          <Link to={"/"}></Link>
        </h1>
       
        <div className="menu" >
          <NavLink className="button" to="/">
            Home
          </NavLink>
          <NavLink className="button" to="/artworks">
            Discover Art
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
            Sign Up
          </NavLink>
          <NavLink className="button" to="/login">
            Log In
          </NavLink>
          <NavLink className="button" to="/about">
            About Us
          </NavLink>
        </div>
      </header>
    
  );
}

export default Nav;
