import React from "react";
import NavBar from './NavBar';
import { Link, NavLink } from "react-router-dom";

function Nav() {
	return (
		<header>
            <h1>
                Mermaid Matisse
                <span className="logo" role="img">
                </span>
            </h1>
			<h1>
				<Link to={"/"}>
					
				</Link>
			</h1>
            <NavBar />
			<div className="menu" >
				<NavLink className="button" to="/artworks" end>
					View All
				</NavLink>
				<NavLink className="button" to="/artists" end>
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
	);
}

export default Nav


// function Nav() {
//     return (
        // <header>
        //     <h1>
        //         Mermaid Matisse
        //         <span className="logo" role="img">
        //         <NavBar />
        //         </span>
        //     </h1>
        // </header>
//     );
// }

// export default Nav

// navlinks here