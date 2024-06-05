#!/usr/bin/node
// print star wars characters title

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const numb = process.argv[2];

request(`${url}${numb}`, function (err, resp, body) {
  console.log(err || JSON.parse(body).title);
});
