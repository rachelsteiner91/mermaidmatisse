import React, { useEffect, useState } from "react";
import {  Route } from "react-router-dom";
import Nav from "./Nav";
// import HomePage from "./HomePage";
import ArtContainer from './ArtContainer';
import Search from './Search'

function App() {
  const [artworks, setArtworks] = useState([])

  useEffect(() => {
      getArtworks();
  },[]);
  
  function getArtworks(){
      fetch ('http://localhost:4000/')
          .then(response => response.json())
          .then(data => setArtworks(data))
  
      }
  // Code goes here!
  return (
    <div className = "app">
      Mermaid Matisse
      <Nav />
      <Search />
      {/* <HomePage /> */}
      
      <Route path="/artworks" element={<ArtContainer artworks={artworks} />}/>
      
    </div>
  )

}

export default App;
