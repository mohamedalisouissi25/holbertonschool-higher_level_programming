#!/usr/bin/node
function fact (arg) {
  if (isNaN(arg) || arg === 1) {
    return 1;
  } else {
    return (arg * fact(arg - 1));
  }
}
const arg = process.argv[2];
console.log(fact(parseInt(arg)));
