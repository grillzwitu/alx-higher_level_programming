#!/usr/bin/node
const myArr = process.argv;
myArr.splice(0, 2);
if (isNaN(myArr[0]) || isNaN(myArr[1])) {
  console.log(0);
} else {
  myArr.sort(function (a, b) { return b - a; });
  console.log(parseInt(myArr[1]));
}
