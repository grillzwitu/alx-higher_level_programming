#!/usr/bin/node
'use strict';
let secMax = 0;
const args = process.argv.slice(2);
let newArr = [];
if (args.length > 1) {
  args.sort();
  for (let arg = 0; arg < args.length; arg++) {
    let numArg = Number(arg);
    newArr.push(numArg);
  }
  secMax = newArr[newArr.length - 2];
}
console.log(secMax);
