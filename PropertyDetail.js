import React from 'react';

export default function PropertyDetail({ property }) {
  if (!property) return <p>Select a property to view details</p>;

  return (
    <div className="card mt-3">
      <div className="card-body">
        <h5 className="card-title">{property.address}</h5>
        <p className="card-text">
          <strong>Rating:</strong> {property.rating}<br />
          <strong>Potential Rating:</strong> {property.potential_rating}<br />
          <strong>Type:</strong> {property.property_type}<br />
          <strong>Built Form:</strong> {property.built_form}<br />
          <strong>Energy:</strong> {property.energy_consumption} kWh<br />
          <strong>CO₂ Emissions:</strong> {property.co2_emissions} t<br />
          <strong>Recommendations:</strong><br />
          <ul>
            {property.recommendations?.map((r, i) => <li key={i}>{r}</li>)}
          </ul>
        </p>
      </div>
    </div>
  );
}