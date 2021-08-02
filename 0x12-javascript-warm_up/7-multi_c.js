#!/usr/bin/node
'use strict';
const noOccurrence = process.argv[2];
if (isNaN(noOccurrence)) {
  console.log('Missing number of occurrences');
} else {
  for (let n = 0; n < noOccurrence; n++) {
    console.log('C is fun');
  }
}
