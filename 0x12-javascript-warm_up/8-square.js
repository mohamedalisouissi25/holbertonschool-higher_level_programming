#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  let d;
  for (d = 0; d < arg; d++) {
    console.log('X'.repeat(arg));
  }
}
