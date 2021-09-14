#!/usr/bin/node
/* Prints all characters in Starwars movie */

const movie = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + movie;
request(url, function (error, response, body) {
  if (!error) {
    const chars = JSON.parse(body).characters;
    printFunc(chars, 0);
  }
});
function printFunc (chars, i) {
  request(chars[i], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (i + 1 < chars.length) {
        printFunc(chars, i + 1);
      }
    }
  });
}
