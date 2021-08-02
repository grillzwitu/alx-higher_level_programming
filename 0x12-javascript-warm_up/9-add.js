#!/usr/bin/node
'use strict';
const x = process.argv[2];
const y = process.argv[3];
function add (x, y) {
  if (isNaN(x) || isNaN(y)) {
    return (NaN);
  } else {
    return (parseInt(x) + parseInt(y));
  }
}
console.log(add(x, y));
