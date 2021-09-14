#!/usr/bin/node
/* display the status code of a GET request */

const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + episode;
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsonobj = JSON.parse(body);
    console.log(jsonobj.title);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
