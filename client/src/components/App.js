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
    if (user === null) {
      fetch('http://localhost:5555/check_session')
        .then(response => {
          if (response.ok) {
            response.json().then(user => {
              setUser(user);
            });
          } else {
            setUser(null)
          }
        })
        .catch(error => {
          console.log(error)
        });
    }
  }, [user]);
  

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
          function onSearchChange(newSearch){
            setSearch(prevSearch => newSearch)
          }
        const filteredArtworks = [...artworks].filter((el) => {
            return el.title.toLowerCase().includes(search.toLowerCase())
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
    <h1 className="extra-bold" style={{}}>
          Mermaid Matisse
          </h1>
      {/* Mermaid Matisse */}
      <Router>
      <Search onSearchChange={onSearchChange} search={search}/>
      <Nav />
      <Routes>
        
        <Route path="/" element={<HomePage artworks={filteredArtworks} />} />
        <Route path="/login" element={<Login />} />
        <Route path="/artworks" element={<ArtContainer artworks={filteredArtworks} addToCollection={addToCollection}/>}/>
        <Route path="/artworks/:id" element={<ArtDetail />} />
        <Route path="/styles" element={<ByStyle styles={filteredStyles}/>} />
        <Route path="/styles/:id" element={<StyleDetail />} />
        <Route path="/artists" element={<Artist artists={filteredArtists} />} />
        <Route path="/artists/:id" element={<ArtistDetail />} />
        <Route path="/collections" element={<Collection collection={collection} />} />
        {/* <Route path="/collections/:id" element={<CollectionDetail />} /> */}
        <Route path="/signup" element={<Signup />} />
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

