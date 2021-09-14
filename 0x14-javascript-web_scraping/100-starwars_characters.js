#!/usr/bin/node
/* Prints all characters of a Starwars movie */

const request = require('request');
const movie = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movie;
request(url, function (error, response, body) {
  if (!error) {
    const chars = JSON.parse(body).characters;
    chars.map(x => request(x, function (error, response, body) {
      if (!error) {
        console.log(JSON.parse(body).name);
      }
    }));
  }
});
