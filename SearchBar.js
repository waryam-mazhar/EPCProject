import React, { useState } from 'react';
import API from '../api';

export default function SearchBar({ onResults }) {
  const [query, setQuery] = useState('');

  const search = () => {
    API.get(`/properties/search?q=${query}`)
      .then(res => onResults(res.data))
      .catch(console.error);
  };

  return (
    <div className="input-group mb-3">
      <input
        type="text"
        className="form-control"
        placeholder="Search by postcode"
        value={query}
        onChange={e => setQuery(e.target.value)}
      />
      <button className="btn btn-outline-primary" onClick={search}>
        Search
      </button>
    </div>
  );
}