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
import UserContext from '../UserContext';
import Login from './Login'
import Search from './Search'
import About from './About'
// import CollectionDetail from './CollectionDetail'


function App() {
  const [user, setUser] = useState(null)
  const [artworks, setArtworks] = useState([])
  const [styles, setStyles] = useState([])
  const [artists, setArtists] = useState([])
  const [collection, setCollection] = useState([]);
  const [search, setSearch] = useState('')
  console.log(user)

  useEffect(() => {
    if (user == null) {
      fetch('/check_session')
      .then(response => {
        if (response.ok) {
          response.json().then(user => {setUser(user)})
        }
      })
    }
  },[user])
 
  useEffect(() => {
      getArtworks();
  },[]);
  
  function getArtworks(){
      fetch ('/artworks')
          .then(response => response.json())
          .then(data => setArtworks(data))
  
      }
      useEffect(() => {
        getStyles();
    },[]);
    
    function getStyles(){
        fetch ('/styles')
            .then(response => response.json())
            .then(data => setStyles(data))
    
        }
        useEffect(() => {
          getArtists();
      },[]);
      
      function getArtists(){
          fetch ('/artists')
              .then(response => response.json())
              .then(data => setArtists(data))
      
          }
          function onSearchChange(newSearch){
            setSearch(prevSearch => newSearch)
          }
        const filteredArtworks = [...artworks].filter((el) => {
            return el.title.toLowerCase().includes(search.toLowerCase()) || el.artists.name.toLowerCase().includes(search.toLowerCase())
      })
        const filteredArtists = [...artists].filter((el) => {
          return el.name.toLowerCase().includes(search.toLowerCase())
        })
        const filteredStyles = [...styles].filter((el) => {
          return el.style_type.toLowerCase().includes(search.toLowerCase())
        })
            
          const addToCollection = (artwork) => {
            artwork.isAdded = true;
            setCollection([...collection, artwork]);
          };
  // Code goes here!
  return (
    <UserContext.Provider value={{user, setUser}}>
    <div className = "app">
    
      {/* Mermaid Matisse */}
      {/* style={{fontWeight: 'extra-bold', position: 'fixed', top: '0', left: '0', width: '100%', backgroundColor: '#fff'}} */}
      <Router>
      <h1 className="extra-bold" style={{fontWeight: 'extra-bold'}}>
          Mermaid Matisse
      </h1>
      <Nav />
      <Search onSearchChange={onSearchChange} search={search}/>
      <Routes>
        
        <Route path="/" element={<HomePage artworks={filteredArtworks} />} />
        <Route path="/login" element={<Login />} />
        <Route path="/artworks" element={<ArtContainer artworks={filteredArtworks} addToCollection={addToCollection}/>}/>
        <Route path="/artworks/:id" element={<ArtDetail />} />
        <Route path="/styles" element={<ByStyle styles={filteredStyles}/>} />
        <Route path="/styles/:id" element={<StyleDetail />} />
        <Route path="/artists" element={<Artist artists={filteredArtists} />} />
        <Route path="/artists/:id" element={<ArtistDetail />} />
        <Route path="/collections" element={<Collection collection={collection}  />} />
        {/* <Route path="/collections/:id" element={<CollectionDetail />} /> */}
        <Route path="/signup" element={<Signup />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
    </div>
    </UserContext.Provider>
  )

}

export default App;

// artist routes:
// <Route path="/artists/:id" element={<ArtistDetail />} />
// <Route path="/artists" element={<Artists artists={artists} />} />
// <Route path="/styles/:id" element={<StyleDetail />} />

