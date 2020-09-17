#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  let d ;
  for (d = 0; d < arg; d++) {
    console.log('C is fun');
  }
}
