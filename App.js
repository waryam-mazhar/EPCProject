import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import PropertyList from './components/PropertyList';
import SearchBar from './components/SearchBar';
import PropertyDetail from './components/PropertyDetail';
import Stats from './components/Stats';

function App() {
  const [properties, setProperties] = useState([]);
  const [selected, setSelected] = useState(null);

  return (
    <div className="container mt-4">
      <h2>EPC Property Explorer</h2>
      <SearchBar onResults={setProperties} />
      <div className="row">
        <div className="col-md-5">
          <PropertyList properties={properties} onSelect={setSelected} />
        </div>
        <div className="col-md-7">
          <PropertyDetail property={selected} />
        </div>
      </div>
      <Stats />
    </div>
  );
}

export default App;