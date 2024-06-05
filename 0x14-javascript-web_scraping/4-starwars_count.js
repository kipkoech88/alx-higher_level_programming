#!/usr/bin/node
// print number of movies with a specific
// character

const request = require('request');
const url = process.argv[2];

request(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
