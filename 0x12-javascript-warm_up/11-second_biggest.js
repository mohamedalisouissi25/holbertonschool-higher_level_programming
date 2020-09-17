#!/usr/bin/node
const arg = process.argv;
if (arg.length === 2 || arg.length === 3) {
  console.log('0');
} else {
  console.log(arg.slice(2).sort((a, b) => b - a)[1]);
}
