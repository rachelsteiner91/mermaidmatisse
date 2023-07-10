import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Nav from "./Nav";
import HomePage from "./HomePage";
import ArtContainer from './ArtContainer';
import Search from './Search'
import ByStyle from './ByStyle'
import ArtDetail from './ArtDetail'
import StyleDetail from './StyleDetail'

function App() {
  const [artworks, setArtworks] = useState([])
  const [styles, setStyles] = useState([])
  console.log(artworks)
  useEffect(() => {
      getArtworks();
  },[]);
  
  function getArtworks(){
      fetch ('http://localhost:5555/artworks')
          .then(response => response.json())
          .then(data => setArtworks(data))
  
      }
      useEffect(() => {
        getStyles();
    },[]);
    
    function getStyles(){
        fetch ('http://localhost:5555/styles')
            .then(response => response.json())
            .then(data => setStyles(data))
    
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
        <Route path="/artworks/:id" element={<ArtDetail />} />
        <Route path="/styles" element={<ByStyle styles={styles}/>} />
        <Route path="/styles/:id" element={<StyleDetail />} />
      </Routes>
    </Router>
    </div>
  )

}

export default App;
