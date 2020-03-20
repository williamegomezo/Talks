import axios from 'axios';
require('dotenv').config();

export default async (req, res) => {
  const {
    query: { name },
  } = req;
  const { ACCESS_TOKEN } = process.env;

  const url = `https://www.superheroapi.com/api.php/${ACCESS_TOKEN}/search/${name}`;
  const response = await axios.get(url);

  res.setHeader('Content-Type', 'application/json')
  res.statusCode = 200
  res.end(JSON.stringify(response.data))
}