import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Nav from "./Nav";
import HomePage from "./HomePage";
import ArtContainer from './ArtContainer';
import ByStyle from './ByStyle'
import ArtDetail from './ArtDetail'
import StyleDetail from './StyleDetail'
import Artist from './Artist'
import ArtistDetail from './ArtistDetail'
import Collection from './Collection'
import Signup from './Signup'
// import CollectionDetail from './CollectionDetail'


function App() {
  const [artworks, setArtworks] = useState([])
  const [styles, setStyles] = useState([])
  const [artists, setArtists] = useState([])
  const [collection, setCollection] = useState([]);
 
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
        useEffect(() => {
          getArtists();
      },[]);
      
      function getArtists(){
          fetch ('http://localhost:5555/artists')
              .then(response => response.json())
              .then(data => setArtists(data))
      
          }
        //   useEffect(() => {
        //     getCollections();
        // },[]);
        
        // function getCollections(){
        //     fetch ('http://localhost:5555/collections')
        //         .then(response => response.json())
        //         .then(data => setCollection(data))
        
        //     }
          const addToCollection = (artwork) => {
            artwork.isAdded = true;
            setCollection([...collection, artwork]);
          };
  // Code goes here!
  return (
    <div className = "app">
      Mermaid Matisse
      <Router>
      <Nav />
      <Routes>
        <Route path="/" element={<HomePage artworks={artworks}/>} />
        <Route path="/artworks" element={<ArtContainer artworks={artworks} addToCollection={addToCollection}/>}/>
        <Route path="/artworks/:id" element={<ArtDetail />} />
        <Route path="/styles" element={<ByStyle styles={styles}/>} />
        <Route path="/styles/:id" element={<StyleDetail />} />
        <Route path="/artists" element={<Artist artists={artists} />} />
        <Route path="/artists/:id" element={<ArtistDetail />} />
        <Route path="/collections" element={<Collection collection={collection} />} />
        {/* <Route path="/collections/:id" element={<CollectionDetail />} /> */}
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </Router>
    </div>
  )

}

export default App;

// artist routes:
// <Route path="/artists/:id" element={<ArtistDetail />} />
// <Route path="/artists" element={<Artists artists={artists} />} />
// <Route path="/styles/:id" element={<StyleDetail />} />

//add images to seed data and models for styles