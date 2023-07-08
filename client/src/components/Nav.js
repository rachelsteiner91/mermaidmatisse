import React from "react";
import { BrowserRouter as Router, Link, NavLink } from "react-router-dom";
import NavBar from './NavBar';

function Nav() {
  return (
    <Router>
      <header>
        <h1>
          Mermaid Matisse
          <span className="logo" role="img"></span>
        </h1>
        <h1>
          <Link to={"/"}></Link>
        </h1>
        <NavBar />
        <div className="menu" >
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
          <NavLink className="button" to="/discovery">
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
    </Router>
  );
}

export default Nav;
