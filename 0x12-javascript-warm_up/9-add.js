#!/usr/bin/node
const i = process.argv[2];
const j = process.argv[3];
function add (i, j) {
  return parseInt(i) + parseInt(j);
}

console.log(add(i, j));
