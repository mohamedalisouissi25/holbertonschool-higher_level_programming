#!/usr/bin/node
const request = require('request');
let comp = 0;
let a = 0;
let b = 0;
request(process.argv[2], function (err, response, body) {
  if (err) { console.log(err); } else {
    const list = JSON.parse(body);
    for (a in list.results) {
      for (b in list.results[a].charachters) {
        if (list.results[a].characters[b].includes('/18/')) {
          comp++;
        }
      }
    }
    console.log(comp);
});
