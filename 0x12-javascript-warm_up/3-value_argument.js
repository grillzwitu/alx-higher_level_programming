#!/usr/bin/node
'use strict';
const i = process.argv[2];
if (i === undefined) {
  console.log('No argument');
} else {
  console.log(i);
}
