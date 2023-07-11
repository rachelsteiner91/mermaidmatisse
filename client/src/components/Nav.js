import React from "react";
import {  Link, NavLink } from "react-router-dom";
import Search from './Search'
// import NavBar from './NavBar';

function Nav() {
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
