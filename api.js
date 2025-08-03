import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'x-api-key': 'test-api-key'
  }
});

export default API;
