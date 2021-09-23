#!/usr/bin/node
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, function (data) {
    data.results.map(
      x => { $('#list_movies').append(`<li>${x.title}</li>`); }
    );
  }
  );
});
