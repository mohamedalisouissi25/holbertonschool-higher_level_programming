#!/usr/bin/node
const list = module.require('./100-data.js').list;
console.log(list);
const list2 = list.map((d, idx) => d * idx);
console.log(list2);
