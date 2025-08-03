import React, { useEffect, useState } from 'react';
import API from '../api';

export default function PropertyList({ onSelect }) {
  const [properties, setProperties] = useState([]);

  useEffect(() => {
    API.get('/properties')
      .then(res => setProperties(res.data))
      .catch(console.error);
  }, []);

  return (
    <div className="list-group">
      {properties.map(prop => (
        <button
          key={prop.uprn}
          onClick={() => onSelect(prop)}
          className="list-group-item list-group-item-action"
        >
          {prop.address} ({prop.rating})
        </button>
      ))}
    </div>
  );
}