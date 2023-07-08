import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Nav from "./Nav";
import HomePage from "./HomePage";
import ArtContainer from './ArtContainer';
import Search from './Search'

function App() {
  const [artworks, setArtworks] = useState([])
  console.log(artworks)
  useEffect(() => {
      getArtworks();
  },[]);
  
  function getArtworks(){
      fetch ('http://localhost:5555/artworks')
          .then(response => response.json())
          .then(data => setArtworks(data))
  
      }
  // Code goes here!
  return (
    <div className = "app">
      Mermaid Matisse
      <Nav />
      <Search />
    <Router>
      <Routes>
        <Route path="/" element={<HomePage artworks={artworks}/>} />
        <Route path="/artworks" element={<ArtContainer artworks={artworks} />}/>
      </Routes>
    </Router>
    </div>
  )

}

export default App;
