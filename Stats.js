import React, { useEffect, useState } from 'react';
import API from '../api';

export default function Stats() {
  const [stats, setStats] = useState({});
  const [top, setTop] = useState([]);

  useEffect(() => {
    API.get('/stats/average-rating').then(res => setStats(res.data));
    API.get('/stats/top-improvements').then(res => setTop(res.data));
  }, []);

  return (
    <div className="mt-4">
      <h5>Statistics</h5>
      <p><strong>Average Rating (numeric):</strong> {stats.average_numeric_rating}</p>
      <ul>
        {top.map((t, i) => (
          <li key={i}>{t.recommendation} ({t.count})</li>
        ))}
      </ul>
    </div>
  );
}