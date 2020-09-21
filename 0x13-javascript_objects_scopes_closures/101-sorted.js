#!/usr/bin/node

const dct = module.require('./101-data.js').dict;
const dct2 = {};
for (const k in dct) {
  if (dct2[dct[k]] !== undefined) {
    dct2[dct[k]].push(k);
  } else {
    dct2[dct[k]] = [k];
  }
}
console.log(dct2);
